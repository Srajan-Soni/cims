from django.urls import path

from teachers import views

urlpatterns = [
    path('teacher/', views.teacher_view),
    path('add_teacher/', views.add_teacher_view),
    path('teacher_pic_upload/', views.teacher_pic_upload_view)
]