"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from shawarma import views
from rest_framework import routers
from shawarma import views

router = routers.DefaultRouter()
router.register(r'shawarmas', views.ShawarmaView, 'shawarmas')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
    path("order/<int:pk>", views.edit_order, name="edit-order"),
    path("about/", views.about, name="about"),
    path("contact", views.contact, name="contact"),

    # This is the path for the API
    # This code specifies the URL path for the API. 
    # This was the final step that completes the building of the API.
    # You can now perform CRUD operations on the Shawarma model. 
    # The router class allows you to make the following queries:
    #
    #
    # /shawarmas/ - returns a list of all the Shawarmas items. 
    # CREATE and READ operations can be performed here.
    # /shawarmas/id - returns a single Todo item using the id primary key. 
    # UPDATE and DELETE operations can be performed here.
    # 
    # Let’s restart the server:
    #   " python manage.py runserver "
    # 
    # Navigate to http://localhost:8000/api/shawarmas in your web browser:
    path('api/', include(router.urls)),

]
