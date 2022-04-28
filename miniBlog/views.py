from django.shortcuts import render
from .models import MiniBlog

# Create your views here.

def Blog(request):
    blog = MiniBlog.objects.order_by('-publisTime')[:5]
    return render(request, 'miniBlog/blog.html', {'blog': blog})