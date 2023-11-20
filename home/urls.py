from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('car_details/<int:car_id>/', views.car_details, name='car_details'),
    path('feedback/', views.feedbackurl, name='feedback'),
    path('main/', views.copyindex, name='main'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('contact/', views.contact, name='contact'),
    path('car-finder/', views.car_finder, name='car-finder'),
    path('news/', views.blog, name='news'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
