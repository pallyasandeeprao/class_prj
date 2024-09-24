from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from .models import Product

# Create your views here.
class Readdata(CreateView):
    model=Product
    fields = '__all__'
    template_name = "read.html"
    context_object_name ="form"
class Display(ListView):
    model=Product
    fields = '__all__'
    template_name = "display.html"
    context_object_name ="form"

class Update(UpdateView):
    model=Product
    fields = '__all__'
    template_name = "read.html"
    context_object_name ="form"

class Delete(DeleteView):
    model=Product
    fields = '__all__'
    template_name = "delete.html"
    context_object_name ="form"
    success_url ='/dis'