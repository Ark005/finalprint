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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
user_language = 'ru'
user_language = 'en'

from django.urls import re_path
from django.views.static import serve

from django.conf import settings
import os
from django.views.static import serve as staticserve




from django.conf.urls import url, include
from cart.models import Cart
from rest_framework import routers, serializers, viewsets

# Сериализаторы описывают представление данных.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity','purchased']

# Наборы представлений описывают поведение представлений.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = UserSerializer

# Роутеры позволяют быстро и просто сконфигурировать адреса.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


from products.views import (
    indexView,
    postProduct, 
    checkNickName,
)


from django.conf.urls import url, include

urlpatterns = [
   
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
 	path('i18n/', include('django.conf.urls.i18n')),
    url(r'^api-auth/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  
]
urlpatterns += i18n_patterns(

   
    path('', include('products.urls', namespace='mainapp')),
 	path('', include('checkout.urls', namespace='checkout')),
    
    path('post/ajax/product', postProduct, name = "post_product"),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('products/account/password_reset.html/', TemplateView.as_view(template_name="products/account/password_reset.html")),
    #path('signup.html/', TemplateView.as_view(template_name="products/signup.html")),
    path('login.html/', TemplateView.as_view(template_name="accounts/login.html")),
    path('reset.html/', TemplateView.as_view(template_name="accounts/password_reset.html")),
    path('register.html/', TemplateView.as_view(template_name="products/register.html")),
    path('account/login.html/', TemplateView.as_view(template_name="products/account/login.html")),
    path('about.html/', TemplateView.as_view(template_name="products/about.html")),
    path('rest.html/', TemplateView.as_view(template_name="products/rest.html")),
    path('support.html/', TemplateView.as_view(template_name="products/support.html")),
    path('calc.html/', TemplateView.as_view(template_name="products/calc.html")),
    path('quality.html/', TemplateView.as_view(template_name="products/quality.html")),
    path('requirements.html/', TemplateView.as_view(template_name="products/requirements.html")),
    path('technologies.html/', TemplateView.as_view(template_name="products/technologies.html")),
    path('layout.html/', TemplateView.as_view(template_name="products/layout.html")),
    path('delivery.html/', TemplateView.as_view(template_name="products/delivery.html")),
    path('photo.html/', TemplateView.as_view(template_name="products/photo.html")),
    path('hmo.html/', TemplateView.as_view(template_name="products/hmo.html")),
    path('terms&conditions.html/', TemplateView.as_view(template_name="products/terms&conditions.html")),
    path('privacy-policy.html/', TemplateView.as_view(template_name="products/privacy-policy.html")),
    path('products_details1.html/', TemplateView.as_view(template_name="products/products_details.html")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    
   # path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()


from django.urls import re_path
from django.views.static import serve

from django.conf import settings
import os
from django.views.static import serve as staticserve


'''

from django.conf.urls import url, include
from cart.models import Cart
from rest_framework import routers, serializers, viewsets

# Сериализаторы описывают представление данных.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity','purchased']

# Наборы представлений описывают поведение представлений.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = UserSerializer

# Роутеры позволяют быстро и просто сконфигурировать адреса.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Привяжите конфигурацию URL, используя роутеры.
# Так же мы предоставляем URL для авторизации в браузере.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
'''