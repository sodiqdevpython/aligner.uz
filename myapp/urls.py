from django.urls import path
from . import views

urlpatterns = [
    path('', views.align_texts, name='align_texts'),  # Matnlarni kiritish interfeysi
    path('check-single-sentence/', views.check_single_sentence, name='check_single_sentence'),  # Har bir gapni tekshirish
]
