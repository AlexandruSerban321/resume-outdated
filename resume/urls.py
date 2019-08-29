from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from curriculum.views import Home_view, home
from post.views import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView
from registration.views import register, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/<int:pk>/details/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('', Home_view, name='home'),
    path('<slug:slug>', home, name='homeurl'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)