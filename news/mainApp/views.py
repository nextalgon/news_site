from django.shortcuts import render
from .models import Category, NewTopic
from django.core.paginator import Paginator
from django.views.generic import DetailView

def index(request):
    topics = NewTopic.objects.all()
    categories = Category.objects.all()
    return render(request, 'mainApp/wrapper.html', {'topics': topics, 'categories': categories})


def category(request, category_id):
    page = request.GET.get('page')
    toifa = Category.objects.get(pk=category_id)
    all_topics = NewTopic.objects.filter(toifasi=toifa)
    paginator = Paginator(all_topics, 6)
    topics = paginator.get_page(page)
    categoriess = Category.objects.all()
    return render(request, 'news/wrapper.html', {'topices': topics, 'categoriess': categoriess})


class MahsulotView(DetailView):
    model = NewTopic
    template_name = "news/Newtopic.html"
