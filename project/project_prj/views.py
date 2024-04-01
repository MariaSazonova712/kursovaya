from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views.generic import DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    tasks = Product.objects.order_by('-id')
    return render(request, 'project_prj/index.html', {
        'title': 'Главная страница сайта', 'tasks': tasks})


class ProductDetailView(DetailView):
    model = Product


def rasp(request):
    return render(request, 'project_prj/rasp.html')


def news(request):
    return render(request, 'project_prj/news.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверно'

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'project_prj/create.html', context)


class Del(DeleteView):
    model = Product
    success_url = '/'
    template_name = 'project_prj/task-delete.html'


class Upd(UpdateView):
    model = Product
    template_name = 'project_prj/create.html'
    form_class = ProductForm
    success_url = '/'


def product_list(request):
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


