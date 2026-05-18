from django.urls import path 
from . import views


urlpatterns=[
    path('', views.landing_view, name='landing_page'),
    path('register',views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('dashboard/',views.DashboardAPIView.as_view(),name='dashboard'),
]