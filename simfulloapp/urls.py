from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('lclinfo', views.lclinfo , name='lclinfo'),
    path('lcladd', views.lcladd , name='lcladd'),
    path('lcldelete', views.lcldelete , name='lcldelete'),
    path('lclupdate', views.lclupdate , name='lclupdate'),
    path('fclinfo', views.fclinfo , name='fclinfo'),
    path('fcladd', views.fcladd , name='fcladd'),
    path('fcldelete', views.fcldelete , name='fcldelete'),
    path('fclupdate', views.fclupdate , name='fclupdate'),
    path('quotation', views.quotation , name='quotation'),
    path('showquote', views.showquote , name='showquote'),
    path('airinfo', views.airinfo , name='airinfo'),
    path('airadd', views.airadd , name='airadd'),
    path('airupdate', views.airupdate , name='airupdate'),
    path('airdelete', views.airdelete , name='airdelete'),
    path('airotheradd', views.airotheradd , name='airotheradd'),
    path('airotheradd', views.airotheradd , name='airotheradd'),
    path('airotherupdate', views.airotherupdate , name='airotherupdate'),
    path('airotherdelete', views.airotherdelete , name='airotherdelete'),
]
