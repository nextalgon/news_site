from django.shortcuts import render
from .models import Category, NewTopic
from django.core.paginator import Paginator
from django.views.generic import DetailView


def index(request):
    topics = NewTopic.objects.all()
    categories = Category.objects.all()
    return render(request, 'mainApp/home.html', {'topics': topics, 'categories': categories})


def category(request, category_id):
    page = request.GET.get('page')
    categ = Category.objects.get(pk=category_id)
    all_topics = NewTopic.objects.filter(category=categ)
    paginator = Paginator(all_topics, 2)
    topics = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'mainApp/home.html', {'categories': categories, 'topics': topics})


class TopicView(DetailView):
    model = NewTopic
    template_name = "mainApp/topic.html"
