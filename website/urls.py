from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.boards, name='boards'),
    url(r'^boards/(?P<pk>\d+)/$', views.contents, name='contents'),
    url(r'^board/new/$', views.board_new, name='board_new'),
]