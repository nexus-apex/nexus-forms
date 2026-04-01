from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('forms/', views.form_list, name='form_list'),
    path('forms/create/', views.form_create, name='form_create'),
    path('forms/<int:pk>/edit/', views.form_edit, name='form_edit'),
    path('forms/<int:pk>/delete/', views.form_delete, name='form_delete'),
    path('formfields/', views.formfield_list, name='formfield_list'),
    path('formfields/create/', views.formfield_create, name='formfield_create'),
    path('formfields/<int:pk>/edit/', views.formfield_edit, name='formfield_edit'),
    path('formfields/<int:pk>/delete/', views.formfield_delete, name='formfield_delete'),
    path('submissions/', views.submission_list, name='submission_list'),
    path('submissions/create/', views.submission_create, name='submission_create'),
    path('submissions/<int:pk>/edit/', views.submission_edit, name='submission_edit'),
    path('submissions/<int:pk>/delete/', views.submission_delete, name='submission_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
