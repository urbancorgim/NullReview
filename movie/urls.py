from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #영화 목록 페이지
    path('create', views.create, name='create'), #영화 등록 페이지
    path('<int:movie_id>', views.detail, name='detail'), #영화 상세 페이지
    path('modify/<int:movie_id>/', views.modify, name='modify'), #영화 수정 페이지
    path('delete/<int:movie_id>', views.delete, name='delete'), #영화 삭제 (링크)
    path('pick/<int:movie_id>', views.pick, name='pick'), #영화 찜하기
]
