from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views as market_views

app_name = "marketplace"
urlpatterns = [
    path('market/', market_views.IndexView.as_view(), name='market_home'),
    path('market/<int:pk>/', market_views.DetailView.as_view(), name="detail"),
    path('market/create_post/', login_required(market_views.PostingCreateView.as_view()), name="make_post"),
    path('market/edit/<int:pk>', market_views.PostingUpdateView.as_view(), name="edit_post"),
    path('market/delete/<int:pk>', market_views.PostingDeleteView.as_view(), name="delete_post"),
    path('market/send_message/<int:posting_id>', login_required(market_views.send_message), name="send_message"),
    path('market/send_message/confirm/', market_views.send_message_confirm, name="send_message_confirm"),
]