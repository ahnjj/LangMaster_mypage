from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, logout_then_login
from django.shortcuts import redirect, render
from .forms import SignupForm

login = LoginView.as_view(template_name='accounts/login_form.html')

def logout(request):
    messages.success(request, '로그아웃되었습니다.')
    return  logout_then_login(request)   # logout한 다음 바로 login페이지로 넘기기
    

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():   # get 인자
            signup_user = form.save()
            # form.save()
            auth_login(request, signup_user)
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next','/')  # 회원가입시 이동할 주소 : 홈
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })