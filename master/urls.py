from django.urls import path
from django.contrib.auth import views as auth_views
from master import views

app_name = 'master'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),            # 홈(관리자목록)
    path('master', views.master, name='master'),    # :8000/master/master
    path('movies', views.movies, name='movies'),    # 영화관리 목록
    path('users', views.users, name='users'),       # 회원관리 목록
    path('superuser/<int:user_id>', views.superuser, name='superuser'),
    path('active/<int:user_id>', views.active, name='active'),
]


