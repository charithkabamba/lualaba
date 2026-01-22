from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.mail import send_mail
import logging
from .models import *

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    services = Service.objects.filter(is_active=True).order_by('title')[:6]
    carousel = Carousel.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'services': services,
        'carousel': carousel,
    }
    return render(request, 'index.html', context)


# about page view
def about(request):
    return render(request, 'management/about.html')

# services page view
def services(request):
    services = Service.objects.filter(is_active=True).order_by('title')
    context = {
        'services': services,
    }
    return render(request, 'management/services.html', context)


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk, is_active=True)
    other_services = Service.objects.filter(is_active=True).exclude(pk=service.pk)[:5]
    context = {
        'service': service,
        'other_services': other_services,
    }
    return render(request, 'management/service_detail.html', context)

# contact
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        phone = request.POST.get('phone')
        project = request.POST.get('project')

        Message.objects.create(
            name=name or '',
            email=email or '',
            subject=subject or '',
            phone=phone or '',
            project=project or '',
            body=body or ''
        )

        # send notification email to site admins (ADMINS) or DEFAULT_FROM_EMAIL
        recipients = []
        if getattr(settings, 'ADMINS', None):
            recipients = [a[1] for a in settings.ADMINS if len(a) > 1]
        elif getattr(settings, 'DEFAULT_FROM_EMAIL', None):
            recipients = [settings.DEFAULT_FROM_EMAIL]

        if recipients:
            subject_email = f"New contact: {subject or 'No subject'}"
            message_email = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Project: {project}\n\n"
                f"Message:\n{body}"
            )
            try:
                send_mail(subject_email, message_email, getattr(settings, 'DEFAULT_FROM_EMAIL', None), recipients)
            except Exception:
                logger.exception('Failed to send contact notification email')

        return redirect('success')
    return render(request, 'management/contact.html')

def feature(request):
    return render(request, 'management/feature.html')

def success(request):
    return render(request, 'management/success.html')
