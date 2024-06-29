from django.urls import path
from . import views, HodViews

urlpatterns = [
    # Authentication URLs
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    
    # Admin home URL
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    
    # Customer management URLs
    path('admin_home/', HodViews.admin_home, name='admin_home'),
    path('manage_crops/', HodViews.manage_crops, name='manage_crops'),
    path('add_crop/', HodViews.add_crop, name='add_crop'),
    path('edit_crop/<int:crop_id>/', HodViews.edit_crop, name='edit_crop'),
    path('delete_crop/<int:crop_id>/', HodViews.delete_crop, name='delete_crop'),

    path('manage_tests/', HodViews.manage_tests, name='manage_tests'),
    path('add_test/', HodViews.add_test, name='add_test'),
    path('edit_test/<int:test_id>/', HodViews.edit_test, name='edit_test'),
    path('delete_test/<int:test_id>/', HodViews.delete_test, name='delete_test'),



    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),



    
    # Admin profile URLs
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
    
]
