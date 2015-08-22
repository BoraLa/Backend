from django.conf.urls import include, url
from Atividades import views

urlpatterns = [
    url(r'^obter_todas_as_atividades/$', views.obter_todas_as_atividades, name="obter_todas_as_atividades"),
    url(r'^atividades_de/(\w+)/$', views.atividades_por_categoria),
    url(r'^tipos_de_atividade_de/(\d+)/$', views.tipos_de_atividade_por_atividade),
]