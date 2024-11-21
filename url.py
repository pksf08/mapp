from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from chat import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.user_list, name="user_list"),
    path("chat/<str:username>/", views.chat_view, name="chat"),
]
