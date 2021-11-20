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

    def get_queryset(self):
        return Posting.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Posting
    template_name = "roommates/detail.html"
