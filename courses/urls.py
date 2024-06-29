from django.urls import path
from . import views


urlpatterns = [
    # views
    path('', views.index, name='index'),
    path('course_description_page/', views.course_description_page, name='course_description_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('request_page/', views.request_page, name='request_page'),
    path('enrolled_courses_page/', views.enrolled_courses_page, name='enrolled_courses_page'),

    # apis
    path('all_courses/', views.all_courses, name='all_courses'),
    path('student_info/', views.student_info, name='student_info'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('get_course_request/', views.get_course_request, name='get_course_request'),
    path('creat_course_request/', views.creat_course_request, name='creat_course_request'),
    path('get_course/', views.get_course, name='get_course'),
]


