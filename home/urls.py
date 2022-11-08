from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    # path('login', views.loginUser),
    # path('logout', views.logoutUser),
    path('contact', views.contact),
]
