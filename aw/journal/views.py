from django.shortcuts import render
from .models import JournalEntry
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import models
from . import forms
# Create your views here.
class CreateEntry(LoginRequiredMixin, generic.CreateView):
    fields = ('date', 'river', 'flow', 'description', 'public')
    model = models.JournalEntry


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')
