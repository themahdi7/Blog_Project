from django.shortcuts import render, redirect
from django.core.mail import send_mail
from blog_app.models import Article
from .forms import MessageForm
from .models import Message, AboutUs, ContactInfo


def home(request):
    articles = Article.objects.filter(Release_Status=True)
    return render(request, "home_app/index.html", {'articles': articles})


def sidebar(request):
    context = {'name': 'sidebar'}
    return render(request, 'includes/sidebar.html', context)


def about_us(request):
    about_us = AboutUs.objects.first()
    return render(request, "home_app/about_us.html", {'about': about_us})


def contact_us(request):
    contact = ContactInfo.objects.first()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            user = request.user
            email = request.user.email
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            Message.objects.create(user=user, name=name, email=email, subject=subject, body=body)
            return redirect('home_app:contact_us')

    else:
        form = MessageForm()
    return render(request, "home_app/contact_us.html", {'form': form, 'contact': contact})
