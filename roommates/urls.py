from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = "roommates"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('create_post/', login_required(views.PostingCreateView.as_view()), name="make_post"),
    path('edit/<int:pk>', views.PostingUpdateView.as_view(), name="edit_post"),
    path('delete/<int:pk>', views.PostingDeleteView.as_view(), name="delete_post"),
    path('send_message/<int:posting_id>', login_required(views.send_message), name="send_message"),
    path('send_message/confirm/', views.send_message_confirm, name="send_message_confirm"),
]
