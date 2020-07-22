from django.contrib import admin
from django.urls import path

from accounts import views as account_views
from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', account_views.login_view, name='login'),
    path('new_game/', views.new_game, name='new_game'),
    path('admin/', admin.site.urls),
    path('game_detail/<int:game_id>', views.game_detail, name='game_detail'),
    path('error/<text>', views.error, name='error'),
]
