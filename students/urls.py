from django.urls import path

from students import views  

urlpatterns = [
    path('dashboard/', views.dashboard_view)
]