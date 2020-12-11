from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home'),
    path('create_request/', views.create_request, name='create_request'),
    path('update_request/<str:pk>', views.update_request, name='update_request'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
