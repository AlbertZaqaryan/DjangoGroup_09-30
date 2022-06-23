from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('<int:id>/', views.HomeDetailView.as_view(), name='home_detail'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout')
]