# -*- coding: utf-8 -*-
from django.utils import translation, timezone, html
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db.models import Q
from main.models import User
from main.models import Language
from main.models import Provider
from main.models import Buyer
from main.models import Topic
from main.models import TopicCategory
from main.models import Sku
from main.models import Plan
from main.models import Order
from main.models import Wallet
from main.models import ReplyToSku
from main.models import ReviewToProvider
from main.models import ReviewToBuyer
from main.models import Log
from main.models import Notification
import datetime

def ds_showtopic(id=0, bywhat=0):
    if bywhat == 0:
        topic = Topic.objects.get(id=id)
    elif id == 0:
        topic = Topic.objects.order_by('bywhat')
    elif bywhat == 0 & id == 0:
        topic = "error"
    return topic


def ds_addlog(
    action,
    user,
    client=0,
    order=None,
    sku=None,
    character=None,
    activity_action=None,
    activity_change=None,
    addtional_title=None,
    addtional_value=None,
    addtional_content=None):
    '''只有增加日志记录功能,
    TYPE_OF_CLIENT = (
        (0, '网页端'),
        (1, '移动网页端'),
        (2, 'IOS客户端'),
        (3, '安卓客户端')
    )
    TYPE_OF_ACTION = (
        (0, '登陆'),
        (1, '登出'),
        (2, '下单'),
        (3, '修改'),
        (4, '取消'),
        (5, '计算劳资'),
        (6, '提取工资'),
        (7, _(u'浏览')),
        (8, _(u'更新课表')),
        (9, _(u'学生订课')), #认为时完成订单支付以后
    )'''
    log = Log(
        client=client,
        action=action,
        user=user,
        order=order,
        sku=sku,
        character=character,
        activity_action=activity_action,
        activity_change=activity_change,
        addtional_title=addtional_title,
        addtional_value=addtional_value,
        addtional_content=addtional_content)
    log.save()
    return log

def ds_getanoti(noti):
    if noti.noti == 0:
        content = u"Your tutor <strong>%s</strong> left a comment:<br/> %s<br>-- from <i>Topic: %s</i>" % (noti.reply.user.provider.name, noti.reply.content, noti.sku.topic.name)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 10:
        content = u"Your student <strong>%s</strong> left a comment:<br/> %s<br>-- from <i>Topic: %s</i>" % (noti.reply.user.buyer.nickname, noti.reply.content, noti.sku.topic.name)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 3:
        content = u"the <strong>%s</strong>'s \" <strong>%s</strong> \" class will begin in 30 mins" % (noti.sku.provider.name, noti.sku.topic.name)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 6:
        content = u"Your teacher <strong>%s</strong> canceled your course:<br/>-- <i>Topic: %s</i>" % (noti.sku.provider.name, noti.sku.topic.name)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 9:
        content = u"Your student %s canceled your course: <br/>-- <i>Topic: %s Time: %s</i>"  % (html.escape(list(noti.sku.buyer.all())), noti.sku.topic, noti.sku.start_time)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 5:
        content = u"Your course's teacher has changed to : <strong>%s</strong><br/>-- <i>Topic: %s</i>" % (noti.sku.provider.name, noti.sku.topic.name)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 8:
        content = u"A student %s booked your course! please confirm and prepare:<br/>-- <i>Topic: %s Time: %s</i>" % (noti.sku.buyer.all().last(), noti.sku.topic.name, noti.sku.start_time)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 2:
        content = u"Your course's plan is ready! please be prepared<br/>-- <i>Topic: %s Time: %s</i>" % (noti.sku.topic.name, noti.sku.start_time)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 7:
        content = u"Your course's plan has been modified! please checkout<br/>-- <i>Topic: %s Time: %s</i>" % (noti.sku.topic.name, noti.sku.start_time)
        link = reverse('main:showsku', args=[noti.sku.id])
    elif noti.noti == 12:
        content = _(u"Your teacher is ready! please checkout <br />-- <i>Link: %s ") % (noti.sku.plan.roomlink)
        link = reverse('main:showsku', args=[noti.sku.id])
    anoti = {'id': noti.id,
             'read' : noti.read,
             'content' : content,
             'open_time': noti.open_time,
             'close_time': noti.close_time,
             'link' : link,
            }
    return anoti

def ds_noti_newreply(reply, user, type):
    noti = 0 if type == 1 else 10
    notification = Notification(user=user,
        reply=reply, sku=reply.sku, open_time = timezone.now(), close_time = timezone.now() + datetime.timedelta(weeks=100), noti=noti)
    notification.save()
    return True

# def ds_noti_newcancel(sku, user, type):
#     noti = 6 if type == 1 else 9
#     notification = Notification(user=user,
#         sku=sku, open_time = timezone.now(),
#         close_time = timezone.now() + datetime.timedelta(weeks=100),
#         noti=noti)
#     notification.save()
#     return True

def ds_get_order_cny_price(skus):
    SKU_CNY_PRICE = 90.00
    if isinstance(skus, Sku):
        cny_price = SKU_CNY_PRICE
    else:
        cny_price = len(skus) * SKU_CNY_PRICE
    return cny_price

def ds_noti_tobuyer_noprovider(sku):
    """给学生发一个 noti 说完蛋了课不上了"""
    for buyer in sku.buyer.all():
        notification = Notification(user=buyer.user, sku=sku,
                                    noti=6, open_time=timezone.now(),
                                    close_time=timezone.now() + datetime.timedelta(weeks=100))
        notification.save()
    return True

def ds_noti_toprovider_lostbuyer(sku):
    """给sku的教师发消息，减少了某学生"""
    notification = Notification(user=sku.provider.user, sku=sku, noti=9,
                                open_time=timezone.now(),
                                close_time=sku.end_time)
    notification.save()
    return True

def ds_change_provider(sku, new_provider):
    """变更教师，传入sku及provider"""
    sku.provider = new_provider
    sku.save()
    ds_noti_tobuyer_changeprovider(sku)
    msg = _(u'教师已变更')
    return msg

def ds_noti_tobuyer_changeprovider(sku):
    """给学生发一个 noti 说课换老师了"""
    for buyer in sku.buyer.all():
        notification = Notification(user=buyer.user, sku=sku,
                                    noti=5, open_time=timezone.now(),
                                    close_time=sku.start_time + datetime.timedelta(hours=1))
        notification.save()
    return True

def ds_noti_toprovider_skubooked(sku):
    """跟教师发通知说sku已被预订"""
    notification = Notification(user=sku.provider.user, sku=sku, noti=8, open_time=timezone.now(),
                                close_time=sku.end_time)
    notification.save()
    return True

def ds_sku_status_check(skus, status):
    '''检查sku的状态是否为可约（0 or 10），能否下单'''
    try:
        if iter(skus):
            for sku in skus:
                if sku.status in status:
                    return True
                else:
                    return False
    except:
        if skus.status in status:
            return True
        else:
            return False

def ds_sku_provider_check(skus, buyer):
    '''检查sku的买家和卖家是否为一个'''
    try:
        if iter(skus):
            for sku in skus:
                if sku.provider.user == buyer.user:
                    return False
                else:
                    return True
    except:
        if skus.provider.user == buyer.user:
            return False
        else:
            return True

def ds_noti_tobuyer_newplan(plan):
    '''通知学生，这节课，老师已经备课完成'''
    for buyer in plan.sku.buyer.all():
        notification = Notification(
            user=buyer.user,
            noti=2,
            sku=plan.sku,
            open_time=timezone.now(),
            close_time=plan.sku.end_time,
            )
        notification.save()
    return True

def ds_noti_tobuyer_planmodified(plan):
    '''通知学生，这节课，老师的教案已修改'''
    for buyer in plan.sku.buyer.all():
        notification = Notification(
            user=buyer.user,
            noti=7,
            sku=plan.sku,
            open_time=timezone.now(),
            close_time=plan.sku.end_time,
            )
        notification.save()
    return True

def ds_noti_tobuyer_skustart(sku):
    '''通知学生，有节课程老师已经准备就绪，可以点击上课链接roomlink了'''
    for buyer in sku.buyer.all():
        notification = Notification(
            user=buyer.user,
            noti=12,
            sku=sku,
            open_time=timezone.now(),
            close_time=sku.end_time,
            note="快上课",
            url=sku.plan.roomlink,
            )
        notification.save()
    return True

def ds_c_provider_in_sku(info, sku):
    '''Check whether the curent user is provider'''
    return bool(info['current_user'].provider == sku.provider)

def ds_c_buyer_in_sku(info, sku):
    '''Check whether the curent user is buyer'''
    return bool(info.get('current_user').buyer in sku.buyer.all())

def ds_c_buyer_in_sku_1(info, sku):
    '''Check whether the curent user is buyer version 1'''
    return bool(sku.buyer.filter(id=info.get('current_user').buyer.id).exists())

def ds_get_review_score(ufq):
    '''返回课程评价得分，满分100，小数四舍五入'''
    score = ((ufq['satisfaction']-1)*20+round((3*4-(ufq['plan']+ufq['teaching']+ufq['continuing']))*100/3))/4
    return round(score)

def ds_lograte(start_from, log_info, days):
    '''读取log_info,返回指定时间段内的登陆次数的比例，即活跃度：登陆的天数/指定时间段 
    算法可改进，循坏开始中后自动跳出并从上一个记录值开始循环（已实现）
    start_info需要date()
    '''
    inday = {}
    logrates = 0
    lt = []
    li = []
    lo = []
    f = {}
    a = 1
    begin_date = (start_from - datetime.timedelta(days=days-1))
    for i in log_info:
        i = i.created

        for x in xrange(a, days+1):
            lo.append(x)
            if i.date() < begin_date+datetime.timedelta(days=x-1):
                break
            elif i.date() == begin_date+datetime.timedelta(days=x-1):
                a = x
                li.append(x)

                inday[x] = 1

                n = begin_date+datetime.timedelta(days=x-1)
                f = {'x':x, 'date':i, 'n':n}
                lt.append(f)
                break

    logrates = float(sum(inday.values()))/days
    assert False
    return logrates

def ds_get_payoff_amount():
    pass

def ds_login_check(user):
    '''for a html browse log which compare the created time of lastest log, 
    if the interval between buyer's activity and timezone.now is less than
    24H and this date has no any activty log.
    then regard the buyer has logined(log:10) once
    '''
    new_log = None
    prov_lc = user.buyer.last_activity
    interval_time = timezone.now() - prov_lc
    lth24 = interval_time <= datetime.timedelta(hours=24)
    gth24 = interval_time > datetime.timedelta(hours=24)
    result = False
    if lth24:
        try:
            log = Log.objects.filter(
                activity_action=10, user=user).order_by('-created')[:1][0]
        except:
            log = None
        try:
            mlog = Log.objects.filter(
                activity_action=-10, user=user).order_by('-created')[:1][0]
        except:
            mlog = None
        # 与非门没掌握好...
        if log is not None:
            istoday = log.created.date() >= timezone.now().date()
            if not istoday:
                result = True
        if mlog is not None:
            mistoday = mlog.created.date() >= timezone.now().date()
            if not mistoday:
                result = True

    elif gth24:
        istoday = False
        mistoday = False
        try:
            log = Log.objects.filter(
                activity_action=10, user=user).order_by('-created')[:1][0]
            istoday = log.created.date() >= timezone.now().date()
        except:
            log = None

        try:
            mlog = Log.objects.filter(
                activity_action=-10, user=user).order_by('-created')[:1][0]
            mistoday = mlog.created.date() >= timezone.now().date()
        except:
            mlog = None

        if (not istoday) or (not mistoday):
            i = interval_time.total_seconds() // (24*3600)
            activity_change = -2*i
            new_log = ds_addlog(
                user=user, action=7, activity_action=-10, activity_change=activity_change)

    if result:
        new_log = ds_addlog(
            user=user, action=7, activity_action=10, activity_change=1)
    # assert False
    return new_log

def ds_log_addacti(log, action):
    '''for add activity imformation to param log'''
    change = 0
    # 进行预处理
    if action==20:
        # 周五前24点更新下周课表+1
        # 未及时更新课表（-5）
        isocal =  timezone.now().isocalendar()
        this_weeknum = isocal[1]
        this_weekday = isocal[2]
        action = None

        if log.addtional_title == 'lastest_schedule_weeknum':
            lastest_schedule_weeknum = log.addtional_value
            gt_this_weeknum = lastest_schedule_weeknum > this_weeknum
            # check the weeknum of log, wether is the next week schedule
            lte_friday = this_weekday < 6
            #  check the whether less than friday.
            if lte_friday and gt_this_weeknum:
                action = 20
            elif not gt_this_weeknum and not lte_friday:
                action =-20
            else:
                return False
            try:
                fit_log = Log.objects.filter(
                    Q(activity_action=action)
                    & Q(addtional_title='lastest_schedule_weeknum')
                    & Q(addtional_value__gte=this_weeknum))
            except:
                fit_log = None
            test1 = fit_log.exists()
            if test1:
                fit_log_exists = fit_log.order_by('-created')[:1][0].created.isocalendar()[1] == this_weeknum
                if fit_log_exists:
                    action = None
                    result = "fit_log_exists"

    if action == 21:
        booked_time = Log.objects.filter(Q(sku=log.sku) & Q(action=9))[0].created
        # 这里有坑，因为book时间是按照sku生成时间计算的，如果出现该sku重新订购的情况，则产生bug
        interval = timezone.now() - booked_time
        if interval.seconds / 3600 < 1:
            action = 21
        elif interval.seconds/3600 > 5:
            action = -21
    # try:
    #     last_same_log = Log.objects.filter(
    #         Q(activity_action=action)).order_by('-created')[:1][0]
    # except:
    #     last_same_log = None
    # if last_same_log is not None:
    #     is_today = last_same_log.created.date() == timezone.now().date()
    #     is_same = last_same_log is log
    # else:
    #     is_today = False
    #     is_same = False
    # if action==None:
    #     return None
    if action == 20 or 21 or 22 or 23 or 24 or 25:
        change = 1
    elif action == 26:
        change = 5
    elif action == -20 or -21:
        change = -5

    if action is not None:
        log.activity_action = action
        log.activity_change = change
        log.save()
        result = '%s, %s' %(action, change)
    # if not is_today and not is_same:
    #     log.activity_action = action
    #     log.activity_change = change
    #     log.save()
    # else:
    #     # assert False
    #     return None

    return log, result



def ds_log_skuaccepted(parameter_list):
    pass
