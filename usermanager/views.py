from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .forms import SignupForm, LoginForm
from .models import User

# Create your views here.


@method_decorator(never_cache,name='dispatch')
class SignupView(View):
    template_name='createuser.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("homeurl")
        return render(request,self.template_name, {'userform': SignupForm()})

    def post(self, request):
        newuser = SignupForm(request.POST, request.FILES)        
        if newuser.is_valid():
            newuser.save()
            return redirect("loginurl")
        return render(request, self.template_name, {'userform': newuser})


@method_decorator(never_cache,name='dispatch')
class HomepageView(LoginRequiredMixin,View):
    login_url='loginurl'
    template_name='home.html'
    def get(self, request):
        users = User.objects.all()
        return render(request,self.template_name, {'users': users})


@method_decorator(never_cache,name='dispatch')
class LoginView(View):
    template_name='login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homeurl')
        form=LoginForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request,form.user)
            return redirect('homeurl')
        return render(request,self.template_name,{"form":form})

class LogoutView(LoginRequiredMixin,View):
    login_url='loginurl'
    def post(self,request):
        logout(request)
        request.session.flush()
        return redirect('loginurl')