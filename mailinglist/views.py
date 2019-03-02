from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

from mailinglist.models import MailingList
from mailinglist.forms import MailingListForm
from mailinglist.mixins import UserCanUseMailingList

class CreateMailingListView(LoginRequiredMixin,CreateView):
    form_class = MailingListForm
    template_name = 'mailinglist/mailinglist_form.html'

    def get_initial(self):
        return {
            'owner': self.request.user.id,
        }

class MailingListListView(LoginRequiredMixin,ListView):

    def get_queryset(self):
        return MailingList.objects.filter(owner=self.request.user)

class MailingListDetailView(LoginRequiredMixin,UserCanUseMailingList,DetailView):
    model = MailingList

class DeleteMailingListView(LoginRequiredMixin,UserCanUseMailingList,DeleteView):
    model = MailingList
    success_url = reverse_lazy('mailinglist:mailinglist_list')
