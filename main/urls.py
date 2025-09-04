from django.urls import path
from django.contrib import admin   # ✅ Import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    

    # ✅ Admin URL
    path('admin/', admin.site.urls),

    
]
