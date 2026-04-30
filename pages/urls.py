from django.urls import path
from .views import PageListView, PageDetailView

app_name = 'pages'

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
]