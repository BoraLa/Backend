from django.conf.urls import include, url
from Atividades import views

urlpatterns = [
    url(r'^obter_todas_as_atividades/$', views.obter_todas_as_atividades, name="obter_todas_as_atividades"),
]