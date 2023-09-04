from django.urls import path
from .views import AprendizView

urlpatterns = [
    path('aprendices/',AprendizView.as_view(), name= 'aprendiz_list'),
    path('aprendices/<int:id>',AprendizView.as_view(), name='aprendiz_process'),
]