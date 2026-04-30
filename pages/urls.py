from django.urls import path
from .views import (
    home, about,
    PageListView, PageDetailView,
    PageCreateView, PageUpdateView, PageDeleteView
)

app_name = 'pages'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),

    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/create/', PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/<int:pk>/update/', PageUpdateView.as_view(), name='page_update'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
]