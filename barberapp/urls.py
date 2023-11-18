"""
URL configuration for barberShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from barberapp.views import BarberappView, ArticleDetailedView, ServicesView, CategoryID, LikeAddView, Services, \
    AppointmentView

app_name = 'barberapp'

urlpatterns = [
    path('', BarberappView.as_view(), name='index'),
    path('post/<int:article_id>/', ArticleDetailedView.as_view(), name='post'),
    path('category/', ServicesView.as_view(), name='categoryes'),
    path('category/<int:category_id>/', CategoryID.as_view(), name='category'),
    path('like/<int:master_id>/', LikeAddView.as_view(), name='like'),
    path('services/<int:master_id>/', Services.as_view(), name='services'),
    path('recording/<int:master_id>/', AppointmentView.as_view(), name='recording'),
]
