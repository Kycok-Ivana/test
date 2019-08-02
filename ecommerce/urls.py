"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from slider.views import by_slider
from news.views import by_news, by_news_single
from products.views import by_product_single
from contacts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', by_news),
    path('<int:id>/', by_news_single, name='single'),
    path('products/<int:id>/', by_product_single, name='single_pr'),
    path('contact/', contactform, name='contact'),
    path('thanks/', thanks, name='thanks'),
    path('photologue/', include('photologue.urls', namespace='photologue')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
