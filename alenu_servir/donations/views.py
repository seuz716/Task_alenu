from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Donacion
from .forms import DonacionForm

class DonationListView(LoginRequiredMixin, ListView):
    model = Donacion
    template_name = 'donations/donation_list.html'
    context_object_name = 'donations'
    paginate_by = 10

class DonationDetailView(LoginRequiredMixin, DetailView):
    model = Donacion
    template_name = 'donations/donation_detail.html'
    context_object_name = 'donation'

class DonationCreateView(LoginRequiredMixin, CreateView):
    model = Donacion
    template_name = 'donations/donation_form.html'
    form_class = DonacionForm
    success_url = reverse_lazy('donations:donation_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class DonationUpdateView(LoginRequiredMixin, UpdateView):
    model = Donacion
    template_name = 'donations/donation_form.html'
    form_class = DonacionForm
    success_url = reverse_lazy('donations:donation_list')

class DonationDeleteView(LoginRequiredMixin, DeleteView):
    model = Donacion
    template_name = 'donations/donation_confirm_delete.html'
    success_url = reverse_lazy('donations:donation_list')
