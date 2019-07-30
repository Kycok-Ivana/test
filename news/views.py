from django.shortcuts import render, get_object_or_404
from .models import News
from slider.models import Slider
from products.models import Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def by_news(request):
    nes = News.objects.all()
    sl = Slider.objects.all()
    pr = Products.objects.all()
    paginator = Paginator(nes, 3)
    page = request.GET.get('page')
    ns = paginator.get_page(page)
    context = {'ns': ns, 'sl': sl, 'pr': pr}
    return render(request, 'index.html', context)

def by_news_single(request, id=None):
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'single_news.html', context)