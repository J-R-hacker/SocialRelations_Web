from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connection
from django.shortcuts import render

from socialdb.models import Socialusers
from .forms.forms import QueryUserForm

'''
@Desc
    视图类
@Author monkey
@Date 2018-04-03
'''
# Create your views here.
def index(request):
    templateView = 'index.html'
    countNum = -1
    keywords = ''
    time = 0

    if request.method == 'GET':

        form = QueryUserForm(request.GET)
        '''
            没有使用 Django 内置组件的验证表单的作用
        # 获得用户输入值
        if 'q' in request.GET and request.GET['q']:

            keywords = request.GET['q']
            print('keywords == ' + keywords)

            # 查询结果
            results = 3
            countNum = 3
            # 查询不到数据, 显示浮窗
            if countNum == 0:
                return render(request, templateView, {
                    'countNum': countNum,
                    'keywords': keywords,
                })
            # 查询到数据, 显示结果
            elif countNum == 3:
                return render(request, templateView, {
                    'countNum': countNum,
                    'keywords': keywords,
                })
        # 直接访问主页, 显示的内容
        else:
            return render(request, templateView, {'countNum': countNum,  'form': form})
        '''
        # 验证表单
        if form.is_valid():
            # 过滤需要的数据
            condition = form.cleaned_data['condition']
            keywords = form.cleaned_data['queryContent']

            print('condition == ' + condition)
            print('keywords == ' + keywords)

            countNum = 0
            # 查询结果
            if condition == 'username':
                user_list = Socialusers.objects.filter(username=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'password':
                user_list = Socialusers.objects.filter(password=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'chineseName':
                user_list = Socialusers.objects.filter(chinesename=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'email':
                user_list = Socialusers.objects.filter(email=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'QQ':
                user_list = Socialusers.objects.filter(qq=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'identity_number':
                user_list = Socialusers.objects.filter(identity_number=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'cell_phone':
                user_list = Socialusers.objects.filter(cell_phone=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'college':
                user_list = Socialusers.objects.filter(college=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })
            elif condition == 'source':
                user_list = Socialusers.objects.filter(source=keywords)
                countNum = user_list.count()
                time = (connection.queries)[0].get('time')
                print('user_list size=== ', user_list.count())
                print('time === ', time)

                # 显示分页操作, 每页显示 20 条
                paginator = Paginator(user_list, 20)
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    # 如果请求的页数不是整数，返回第一页。
                    users = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    users = paginator.page(paginator.num_pages)

                return render(request, templateView, {
                        'countNum': countNum,
                        'condition': condition,
                        'keywords': keywords,
                        'form': form,
                        'users': users,
                        'time': time,
                    })

            # 查询不到数据, 显示没有数据的浮窗
            if countNum == 0:
                return render(request, templateView, {
                    'countNum': countNum,
                    'keywords': keywords,
                    'form': form,
                })
        # 直接访问主页, 显示的内容
        else:
            return render(request, templateView, {'countNum': countNum,  'form': form})
