from django.urls import path

from institutes import views

urlpatterns = [
    #path('signup/', views.signup_view),
    #path('check_username/', views.check_username_view),
    path('activate_account/', views.activate_account_view),    
    path('profile/', views.profile_view),
    path('profile_logo_upload/', views.profile_logo_upload_view),
    path('dashboard/', views.dashboard_view),
    path('pics/', views.pics_view),
    path('institute_pics_upload/<int:pic_type_id>', views.institute_pics_upload_view),
    path('courses/', views.courses_view),
    path('course_pic_upload/', views.course_pic_upload_view),
    path('course_syllabus_upload/', views.course_syllabus_upload_view),
    path('batches/', views.batches_view),
    path('search/', views.search_view)
]