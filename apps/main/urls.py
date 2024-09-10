from django.urls import path
from .views import home_view, about_view, certificate_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('certificates/', certificate_view, name='certificates'),
]
