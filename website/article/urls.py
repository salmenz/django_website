from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    #/article/
    path('', views.index, name='index'),

    #/article/$id
    path('<int:article_id>/', views.detail, name='detail'),

]