
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    # path("login/",views.user_login, name="login"),
    path("login/",auth_views.LoginView.as_view(), name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name = "registration/logout.html"), name="logout"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("password-change/",auth_views.PasswordChangeView.as_view(template_name="account/password_change_form.html") ,name="password_change"),
    path("password_change_done/",auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),name="password_change_done"),
    path("edit/",views.edit,name="edit"),

    #password reset


    path("password-reset/",auth_views.PasswordResetView.as_view(template_name="account/password_reset_form.html"),name="password_reset"),
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"),name="password_reset_confirm"),
    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),name="password_reset_complete"),


    path("", include("django.contrib.auth.urls")),
    path("register/",views.register,name="register"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)