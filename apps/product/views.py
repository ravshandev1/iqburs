from django.shortcuts import render, redirect
from .models import Category, Product
from main.models import BotMessage, Application
from django.http import JsonResponse
from django.conf import settings
from requests import post
from pytz import timezone
from django.contrib import messages


def products_view(request):
    categories = Category.objects.all()
    cat = categories[0]
    products = Product.objects.filter(category=cat)
    return render(request, 'catalog.html', {'categories': categories, 'products': products})


def product_list(request):
    category_name = request.GET.get('cat')
    products = Product.objects.filter(category__name__exact=category_name)
    product_data = [{
        'id': product.id,
        'name': product.name,
        'iso_number': product.iso_number,
        'image_url': product.image.url,
    } for product in products]

    return JsonResponse({'products': product_data})


def product_view(request, pk):
    product = Product.objects.filter(pk=pk).first()
    similar_products = Product.objects.filter(category_id=product.category_id).exclude(id=pk)
    if request.method == 'POST':
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        obj = Application.objects.create(phone=phone, name=name)
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
        messages.success(request, 'Success')
        return redirect('.')
    return render(request, 'product.html', {'product': product, 'similar_products': similar_products})
