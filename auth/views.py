from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RegForm
from userprofile.models import Profile

# Create your views here.
def index(request):
    reg_form = RegForm()
    return render(request, 'registration/reg.html', {'reg_form': reg_form})


def create_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    User.objects.create_user(username=username, email=email, password=password)
    Profile.objects.auto_created
    return HttpResponseRedirect(reverse('login'))
