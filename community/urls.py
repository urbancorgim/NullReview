from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'community'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),          #목록보기
    path('post/', views.board_post, name='post'), #등록하기
    path('detail/<int:post_id>', views.board_detail, name='detail'), #상세 보기
    path('modify/<int:post_id>', views.board_modify, name='modify'), #수정
    path('delete/<int:post_id>', views.board_delete, name='delete'), #삭제

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)