# -*- coding: utf-8 -*-
 
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from main.act import act_signup
from main.act import act_jisuan
from main.act import act_addlanguage
from main.act import act_showuser
# from main.act import 

def url_signup_post(request):
# "用户通过浏览器将表单内容post到/signup/post后来到这里"
    # word = act_return_check()
    # word = act_signup()
    # if request.method == 'POST':
    #     act_signup(username, password, email, )
    pass

def url_index(request,fuckset):
    boy=int(fuckset)
    # return render(request, 'pass', )
    ace=act_jisuan(boy)
    return HttpResponse(ace)

def url_user(request,offset):
    id = int(offset)
    user = act_showuser(id)
    username = user.username
    email = user.email 
    password = user.password
    result = username + email + password
    return HttpResponse(result)

def url_test_set(request,offset = 0 ):
    set = int(offset)
    act = test_signup(set)
    return HttpResponse(act)













def test_signup(set):
    if set == 0:
        b = act_signup(
        email= "swee@msn.com",
        password = "123",
        nickname = "Bob",
        gender = "1",
        mother_tongue_id = 1,
        time_zone = 'America/Chicago')
    else:
        b = act_signup(
        email= str(set) + "swee@msn.com",
        password = "123",
        nickname = "Bob",
        gender = "1",
        mother_tongue_id = 1,
        time_zone = 'America/Chicago')
    return b

def test_addlanguage(set):
    if set == 0:
        result = act_addlanguage(
        english_name = str(set) + "english",
        chinese_name = str(set) + "英语",
        local_name = str(set) + "英语")
    else:
        result = act_addlanguage(
        english_name = "english",
        chinese_name = "英语",
        local_name = "英语")
    return result
