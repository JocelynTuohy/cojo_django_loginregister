# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    print 'Earth Angel, Earth Angel, Please be mine, my darling dear...'
    return render(request, 'loginregister/index.html')

def validate(request):
    # print 'ready to validate!'
    if request.method=='POST':
        # print 'POSTED!'
        userobject = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'confirm': request.POST['confirm']
        }
        errors = User.objects.validate(userobject)
        if errors:
            # print errors
            for each in errors:
                messages.error(request, each)
        else:
            # print 'things!'
            newuser = User.objects.create(
                first_name=userobject['first_name'],
                last_name=userobject['last_name'],
                email=userobject['email'],
                password=(
                    bcrypt.hashpw(userobject['password'].encode(), 
                                  bcrypt.gensalt())
                )
            )
            request.session['id'] = newuser.id
            return redirect('/register')
    return redirect('/')

def register(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'first_name': user.first_name,
        'achievement': 'registered'
    }
    return render(request, 'loginregister/success.html', context)

def verify(request):
    if request.method=='POST':
        logobject = {
            'email': request.POST['log_email'],
            'password': request.POST['log_password']
        }
        verification = User.objects.verify(logobject)
        if verification['errors']:
            for each in verification['errors']:
                messages.error(request, each)
        else:
            request.session['id'] = verification['id']
            return redirect('/login')
    return redirect('/')

def login(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'first_name': user.first_name,
        'achievement': 'logged in'
    }
    return render(request, 'loginregister/success.html', context)

