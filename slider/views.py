from django.shortcuts import render
from .models import Slider
# Create your views here.
def by_slider(request):
    sl = Slider.objects.all()
    context = {'sl': sl}
    return render(request, 'index.html', context)