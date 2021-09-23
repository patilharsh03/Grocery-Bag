from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Grocery

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('groceries')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm      
    redirect_authenticated_user = True
    success_url = reverse_lazy('groceries')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('groceries')
        return super(RegisterPage, self).get(*args, **kwargs)        

class GroceryList(LoginRequiredMixin, ListView):
    model = Grocery
    context_object_name = 'groceries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['groceries'].filter(user=self.request.user)
        context['count'] = context['groceries'].filter(choose=False).count()
        return context
    

class GroceryDetail(LoginRequiredMixin, DetailView):
    model = Grocery
    context_object_name = 'grocery'

class GroceryCreate(LoginRequiredMixin, CreateView): 
    model = Grocery
    fields = ['item_name', 'item_quantity', 'choose', 'date']
    success_url = reverse_lazy('groceries')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GroceryCreate, self).form_valid(form)

class GroceryUpdate(LoginRequiredMixin, UpdateView):
    model = Grocery   
    fields = ['item_name', 'item_quantity', 'choose', 'date']
    success_url = reverse_lazy('groceries') 

class GroceryDelete(LoginRequiredMixin, DeleteView):
    model = Grocery
    context_object_name = 'grocery'   
    success_url = reverse_lazy('groceries')  