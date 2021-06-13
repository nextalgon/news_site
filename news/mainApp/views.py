from django.shortcuts import render
from .models import Category, NewTopic
from django.core.paginator import Paginator
from django.views.generic import DetailView, TemplateView


def index(request):
    topics = NewTopic.objects.all()[:5]
    categories = Category.objects.all()
    return render(request, 'mainApp/home.html', {'topics': topics, 'categories': categories})


def category(request, category_id):
    page = request.GET.get('page')
    categ = Category.objects.get(pk=category_id)
    all_topics = NewTopic.objects.filter(category=categ)
    paginator = Paginator(all_topics, 2)
    topics = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'mainApp/category.html', {'categories': categories, 'topics': topics})


class TopicView(DetailView):
    model = NewTopic
    template_name = "mainApp/topic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class TeamPage(TemplateView):
    template_name = 'mainApp/teamPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
