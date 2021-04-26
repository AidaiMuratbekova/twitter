from django.urls import path
from . import views
from .views import *

app_name = 'blog'
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('<int:year>/<int:month>/<int:day>/<slug:post>/',
#          views.post_detail, name='post_detail'),
# ]
urlpatterns = [
    path('', index, name='home'),
    path('', category_detail, name='category'),
    path('', views.post_list, name='post_list'),
    path('', post_detail, name='detail'),
    path('add-post/', add_post, name='add-post'),
    path('', views.PostPageView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),


]

