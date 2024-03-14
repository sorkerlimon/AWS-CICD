from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ApplyFormForm
from django.contrib import messages
from .models import *
from django.http import JsonResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
import random
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.files.base import ContentFile
import cv2
from datetime import datetime

# Create your views here.

def jobapply(request):
    if request.method == 'POST':
        form = ApplyFormForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            if ApplyForm.objects.filter(email=email).exists():
                messages.error(request, 'This email is already in use. Please use a different email.')
            else:
                form.save()
                form = ApplyFormForm()

            
        else:
            print("Form errors:", form.errors)
    else:
        form = ApplyFormForm()

    return render(request, 'iimijob/apply.html', {'form': form})

def license(request):
    return render(request, 'iimijob/license.html')
