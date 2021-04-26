"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib import admin

from accounts.views import ProfilePage, RegisterView, SuccessRegistrationView
from blog import views
from blog.views import index, category_detail, post_detail, add_post, SearchResultsView, PostPageView, PostDeleteView

urlpatterns = [

    path('admin/', admin.site.urls),

    path('blog/', include('blog.urls', namespace='blog')),
    path('blog/', index, name='home'),
    path('', category_detail, name='category'),
    path('', post_detail, name='detail'),
    path('add-post/', add_post, name='add-post'),
    path('', PostPageView.as_view(), name='post_list'),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    url(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    path('register/successful_registration/', SuccessRegistrationView.as_view(), name="successful-registration"),
    path('blog/search', SearchResultsView.as_view(), name='search-results'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

