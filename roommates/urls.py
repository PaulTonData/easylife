from django.urls import path
from . import views

app_name = "roommates"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('create_post/', views.PostingCreateView.as_view(), name="make_post"),
    path('edit/<int:pk>', views.PostingUpdateView.as_view(), name="edit_post"),
    path('delete/<int:pk>', views.PostingDeleteView.as_view(), name="delete_post"),
]
