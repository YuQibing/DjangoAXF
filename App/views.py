from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from App.models import *


def home(request):
    wheelList = Wheel.objects.all()
    navList = Nav.objects.all()
    buyList = Mustbuy.objects.all()
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]

    mainList = MainShow.objects.all()
    context = {'pagetitle': '首页', 'wheelList': wheelList, 'navList': navList, 'buyList': buyList, "shop1": shop1, "shop2": shop2, "shop3": shop3, "shop4": shop4, "mainList": mainList}
    return render(request, 'App/home.html', context)


# def market(request):
#     foodTypes = FoodTypes.objects.all()
#     goodsList = Goods.objects.filter(categoryid=104749)
#     context = {'pagetitle': '闪购', 'foodTypes': foodTypes, 'goodsList': goodsList}
#     # return HttpResponse(context)
#     return render(request, 'App/market.html', context)
    # return render(request, 'App/market.html', context)


def market(request, foodtype, childcid, ording):
    foodTypes = FoodTypes.objects.all()
    if ording == '0':
        orderRule = 'id'
    elif ording == '1':
        orderRule = 'price'
    else:
        orderRule = '-price'

    if childcid == '0':
        goodsList = Goods.objects.all().filter(categoryid=foodtype).order_by(orderRule)
    else:
        goodsList = Goods.objects.all().filter(categoryid=foodtype).filter(childcid=childcid).order_by(orderRule)

    childType = FoodTypes.objects.filter(typeid=foodtype)

    groupList = []
    for i in childType:
        list = i.childtypenames.split('#')
        for j in list:
            group = {'childName': j.split(':')[0], 'childType': j.split(':')[1]}
            groupList.append(group)

    context = {'pagetitle': '闪购', 'foodTypes': foodTypes, 'goodsList': goodsList, 'childType': groupList, 'foodType': foodtype, 'childcid': childcid}
    return render(request, 'App/market.html', context)

def cart(request):
    context = {'pagetitle': '购物车'}
    return render(request, 'App/cart.html', context)


def mine(request):
    context = {'pagetitle': '我的'}
    return render(request, 'App/mine.html', context)


def user(request):
    accountCookie = request.COOKIES.get('user')
    if accountCookie:
        user = User.objects.filter(userAccount=accountCookie)[0]
        context = {'account': user}
        response = render(request, 'App/mine.html', context)
        return response
    else:
        return render(request, 'App/user.html')


def checkAccount(request):
    account = request.GET.get('account')
    length = len(User.objects.filter(userAccount=account))
    if length == 0:
        context = {'status': '用户可以注册'}
    else:
        context = {'status': '用户已经存在'}

    return JsonResponse(context)

def createAccount(request):
    account = request.GET.get('userAccount')
    passwd = request.GET.get('userPassword')
    user = User.createuser(account, passwd)
    user.save()
    context = {'account': user}
    # response = HttpResponseRedirect(reverse('axf:mine', user))
    # response.set_cookie('user', account, max_age=1000)
    # return render(request, 'App/mine.html', context)
    response = render(request, 'App/mine.html', context)
    return response


def login(request):
    response = render(request, 'App/login.html')
    response.delete_cookie('user')
    return response


def doLogin(request):
    account = request.GET.get('userAccount')
    passwd = request.GET.get('userPassword')
    user = User.objects.all()
    count = 0
    for i in user:
        if i.userAccount == account:
            if i.userPasswd == passwd:
                context = {'account': i}
                # request.session['user'] = context
                # response = HttpResponseRedirect(reverse('axf:mine', i))
                # response.set_cookie('user', account, max_age=1000)
                # return response
                response = render(request, 'App/mine.html', context)
                response.set_cookie(key='user', value=account, max_age=1000)
                return response

            else:
                return HttpResponse('password error')

        else:
            count += 1
            if count == len(user):
                return HttpResponse('no user')
            else:
                continue


