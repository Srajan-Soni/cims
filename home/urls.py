from django.urls import path

from home import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index_view),
    path('sendotp/', views.send_otp_view),
    path('check_otp/', views.check_otp_view),
    path('cities/', views.city_list_view),
    path('login/', views.login_view),
    path('signup/', views.signup_view),
    path('signup_success/', TemplateView.as_view(template_name='signup_success.html')),
    path('check_username/', views.check_username_view),
    path('user_city/', views.user_city_view)
]