from django.shortcuts import render, redirect
from .models import Certificate, Carousel, Feedback, About, BotMessage, Advantage, Application
from requests import post
from django.conf import settings
from product.models import Product
from pytz import timezone
from django.contrib import messages


def home_view(req):
    carousels = Carousel.objects.all()
    products = Product.objects.all()[:8]
    feedbacks = Feedback.objects.all()
    advantages = Advantage.objects.all()
    if req.method == 'POST':
        phone = req.POST.get('phone')
        name = req.POST.get('name')
        obj = Application.objects.create(name=name, phone=phone)
        text = f"Ism: {obj.name}\n"
        text += f"Telefon: {obj.phone}\n"
        text += f"Javob berildi: ❌\n"
        text += f"Yuborilgan vaqt: {obj.created_at.astimezone(tz=timezone('Asia/Tashkent')).strftime('%d.%m.%Y %H:%M')}"
        payload = {
            "chat_id": settings.GROUP_ID,
            "text": text,
            "parse_mode": "HTML"
        }
        res = post(f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage", json=payload)
        BotMessage.objects.create(application_id=obj.id, message_id=res.json()['result']['message_id'])
        messages.success(req, "Success")
        return redirect('.')
    return render(req, 'index.html',
                  {'advantages': advantages, 'carousels': carousels, 'products': products, 'feedbacks': feedbacks})


def about_view(req):
    obj = About.objects.first()
    return render(req, 'about.html', {'obj': obj})


def certificate_view(req):
    qs = Certificate.objects.all()
    return render(req, 'certificate.html', {'qs': qs})
