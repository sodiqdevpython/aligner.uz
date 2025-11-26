# urls.py
from django.urls import path
from .views import gpt_align, align_texts

urlpatterns = [
    path('', align_texts, name='align_texts'),
    path('gpt-align/', gpt_align, name='gpt_align'),
]
