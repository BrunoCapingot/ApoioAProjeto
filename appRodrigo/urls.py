from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('template_gerente/', views.template_gerente, name='template_gerente'),
    #path('', views.template_tester, name='template_tester'),
    #path('', views.template_desenvolvedor, name='template_desenvolvedor'),
    #path('identificacao/', views.identificadores_view, name='identificacao'),
    #path('sistema_de_cameras/', views.sistema_de_cameras, name='sistema_de_cameras'),
    #path('gravar_frames/', views.gravar_frames, name='gravar_frames'),
    #path('upload_video/', views.upload_video, name='upload_video'),
    #path('lista_de_classes/', views.lista_de_classes, name='lista_de_classes'),
    #path('resultado_identificacao/', views.resultado_identificacao, name='resultado_identificacao'),
    #path('classe/<str:nome>/', views.detalhe_classe, name='detalhe_classe'),

]
