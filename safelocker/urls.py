from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('login', views.login_user, name='login-page'),
    path('register-user', views.register_user, name='register-page'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('logout', views.logout_user, name='logout'),

    path('user-locker', views.user_locker, name='user-locker'),
    path('user-locker/item-selected/<str:pk>', views.selected_item, name='selected-item'),
    path('save-to-locker', views.locker_form, name='locker-form'),
    path('edit-item/<int:pk>/', views.edit_item, name='edit-item'),

    path('delete-item/<int:pk>/', views.delete_item, name='delete-item'),
    path('delete-profile/<int:pk>/', views.delete_profile, name='delete-profile'),
]
