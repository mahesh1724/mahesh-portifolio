from django.shortcuts import render, redirect
from .models import VisitorLog
from django.utils.timezone import now, localtime
import uuid

def generate_uid(request):
    new_uid = uuid.uuid4()
    return redirect('home', uid=new_uid)

def redirect_with_uid(request, page):
    new_uid = uuid.uuid4()
    return redirect(page, uid=new_uid)

def home(request, uid):
    ip = get_client_ip(request)

    # Convert time to Indian time
    current_time = localtime(now())  # IST time
    VisitorLog.objects.create(ip_address=ip, timestamp=current_time)

    # Optional: Print/log the visit
    print(f"{ip} at {current_time}")  # Shows IST time like "192.168.1.36 at 2025-06-14 15:05:00+05:30"

    return render(request, 'portfolio/home.html', {'uid': uid})

def profile(request, uid):
    return render(request, 'portfolio/profile.html', {'uid': uid})

def projects(request, uid):
    return render(request, 'portfolio/projects.html', {'uid': uid})

def achievements(request, uid):
    return render(request, 'portfolio/achievements.html', {'uid': uid})

def contact(request, uid):
    return render(request, 'portfolio/contact.html', {'uid': uid})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
