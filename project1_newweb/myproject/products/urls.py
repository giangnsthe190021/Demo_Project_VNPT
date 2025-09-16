from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create-admin/', views.create_admin, name='create_admin'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_user, name='update_user'),
    path('user/<int:user_id>/', views.view_user_profile, name='view_user_profile'),
    path('create-course/', views.create_course, name='create_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/upload/', views.upload_question_file, name='upload_question_file'),
    path('course/<int:course_id>/delete-file/<int:file_id>/', views.delete_question_file, name='delete_question_file'),
    path('course/<int:course_id>/quiz/<int:file_id>/', views.quiz_from_file, name='quiz_from_file'),
    path('course/<int:course_id>/flashcards/<int:file_id>/', views.flashcards_from_file, name='flashcards_from_file'),
    path('course/<int:course_id>/enrollments/', views.manage_enrollments, name='manage_enrollments'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),    
]