from typing import Any
from django import http
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm 

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs): 
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
 
# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    #def get_success_url(self):               #este es uno de los metodos para retornar a la vista después de guardar
    #    return reverse('pages:pages')        #configuramos la pagina a la que retornara una vez que guardamos el formulario

@method_decorator(staff_member_required, name='dispatch')    
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
@method_decorator(staff_member_required, name='dispatch')    
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')