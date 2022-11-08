# from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.index),
    path('new',views.new),
    path('show',views.show),
    path('edit/<int:id>', views.edit),

    path('create', views.create),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
