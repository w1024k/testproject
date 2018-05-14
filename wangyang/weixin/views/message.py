# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from weixin import settings, tasks
import wechatpy
from common.tools import auto_answer


def notify(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        try:
            check_signature(settings.TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            return HttpResponse('')
        return HttpResponse(echostr)
    else:
        receive_msg = wechatpy.parse_message(request.body)
        # 收到文本,自动回复
        if isinstance(receive_msg, wechatpy.messages.TextMessage):
            content = auto_answer.answer_robot(receive_msg.content)
            reply = wechatpy.replies.TextReply(content=content, message=receive_msg)
            return HttpResponse(reply.render())
        # 关注事件
        elif isinstance(receive_msg, wechatpy.events.SubscribeEvent):
            receive_msg.msgtype = 'text'
            reply = wechatpy.replies.TextReply(content=settings.ANSWER_MSG_LIST['SUBSCRIBE'], message=receive_msg)
            tasks.create_weixin_user.delay(receive_msg.source)
            return HttpResponse(reply.render())
        # 取消关注
        elif isinstance(receive_msg, wechatpy.events.UnsubscribeEvent):
            print receive_msg.source
            return HttpResponse('')

        # 扫描带参数二维码(已关注,未关注,未关注微信会提示关注) 可用于扫码登录
        elif isinstance(receive_msg, (wechatpy.events.ScanEvent, wechatpy.events.SubscribeScanEvent)):
            return HttpResponse('')

        else:
            receive_msg.msgtype = 'text'
            reply = wechatpy.replies.TextReply(content=settings.ANSWER_MSG_LIST['PARSE_FAIL'], message=receive_msg)
            return HttpResponse(reply.render())