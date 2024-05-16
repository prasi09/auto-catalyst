from django.urls import path,include
from . import views

app_name='users'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('agent_register/', views.agent_register_view, name="agent_register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('activate/<str:uidb64>/<str:token>/',views.activate,name="activate"),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
]