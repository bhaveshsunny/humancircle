from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .forms import ProfileForm, PhotoForm, Signupform, LoginForm, EventForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from app.models import Profile, Bookdate, Event
from datetime import date, timedelta

user_form = LoginForm()
admin_form = LoginForm()
def index(request):
    return  render(request, 'app/index.html',{'user_form': user_form,'admin_form': admin_form})

def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.clean()
            form.login(request)
            if request.user.is_staff:
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
    else:
        return redirect('index')
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.clean()
            form.login(request)
            return redirect('user_dashboard')
    else:
        return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

@staff_member_required
def admin_dashboard(request):
    return  render(request, 'app/admin.html')

def register(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = Signupform()
    return render(request, 'app/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return redirect('user_dashboard')
    else:
        form = ProfileForm()
    return render(request, 'app/profile.html', {'form': form})

@login_required
def user_dashboard(request):
    if request.method == 'POST':
        Profile.objects.filter(user=request.user).delete()
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return redirect('user_dashboard')
    else:
        form = ProfileForm()
        eventform = EventForm()
        status = {}
        status['payment'] = "Not Payed"
        try:
            interview = Bookdate.objects.get(user=request.user)
            if interview.approved:
                status['interview'] = "Confirmed"
            if interview.rejected:
                status['interview'] = "Rejected, apply for different event."
            else:
                status['interview'] = "Pending"
        except Bookdate.DoesNotExist:
            interview = Bookdate.objects.create(user=request.user)
            status['interview'] = "not Applied for any Event"
        try:
            profile = Profile.objects.get(user=request.user)
            status['profile'] = "Filled"
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=request.user)
            status['profile'] = "not Filled"

        return  render(request, 'app/dashboard.html',{'profile':profile,'form':form,'eventform':eventform,'status':status})

@login_required
def event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return redirect('user_dashboard')
    else:
        return redirect('user_dashboard')


def model_form_upload(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'app/model_form_upload.html', {
        'form': form
    })


from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'app/photo_list.html', {'form': form, 'photos': photos})
