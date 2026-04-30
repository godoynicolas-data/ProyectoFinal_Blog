from django.urls import path
from .views import inbox_view, sent_view, compose_message_view, message_detail_view

app_name = 'messaging'

urlpatterns = [
    path('inbox/', inbox_view, name='inbox'),
    path('sent/', sent_view, name='sent'),
    path('compose/', compose_message_view, name='compose'),
    path('<int:pk>/', message_detail_view, name='detail'),
]