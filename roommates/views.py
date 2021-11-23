from django.core.mail import send_mail, BadHeaderError
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .forms import MessageForm
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

    def form_valid(self, form):
        self.object = form.save(commit=False)

        if self.request.user.is_authenticated:
            self.object.user = self.request.user
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise Exception("no user logged in")

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

def send_message(request, posting_id):
    posting = get_object_or_404(Posting, pk=posting_id)

    if request.method == 'GET':
        form = MessageForm()
    else:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            try:
                user_email = request.user.email
                subject = f"{user_email} is interested in your post on EasyLife!"
                send_mail(subject, message, from_email="admin@stevenseasylife.com", recipient_list=[posting.user.email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('roommates:send_message_confirm'))
    return render(request, 'roommates/send_message.html', {'form': form})

def send_message_confirm(request):
    return render(request, 'roommates/send_message_confirm.html')
