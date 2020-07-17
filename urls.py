from django.urls import path

from accounts import views as account_views
from game import views

urlpatterns = [
    path('', views.main),
    path('accounts/login/', account_views.login_view, name='login')
]