from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Posting, Photo

class IndexView(generic.ListView):
    template_name = "roommates/index.html"
    context_object_name = "posting_list"

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits
        context["num_visits"] = num_visits
        return context
    """

    def get_queryset(self):
        return Posting.objects.all()[:5]

class PostingCreateView(generic.edit.CreateView):
    model = Posting
    fields = ['title', 'rent', 'distance_time', 'distance_mode', 'description']

class PostingUpdateView(generic.edit.UpdateView):
    model = Posting
    fields = ['title', 'rent', 'distance_time', 'distance_mode', 'description']

class PostingDeleteView(generic.edit.DeleteView):
    model = Posting
    def get_success_url(self):
        return "/"

class DetailView(generic.DetailView):
    model = Posting
    template_name = "roommates/detail.html"
