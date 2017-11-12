from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View

from .models import UserProfile
from .forms import LoginForm
# Create your views here.

#class CustomBackend(ModelBackend):
#    def authenticate(self, username=None, password=None, **kwargs):
#        try:
#            # why: 无法实现邮箱登陆
#            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
#            if user.check_password(password):
#                return user
#        except Exception as e:
#            print('not found user')
#            return None

class LoginView(View):
    def get(self, request):
        index_page = render(request, 'login.html')
        return index_page
    
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid(): # 插入一个表单用于做验证
            user_name = login_form.cleaned_data.get('username')
            pass_word = login_form.cleaned_data.get('passname')

            #user_name = request.POST.get('username', '')
            #pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word) # 返回当前用户
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {"msg": "用户名或密码错误"})
        else:
            return render(request, 'login.html', {"login_form":login_form})
