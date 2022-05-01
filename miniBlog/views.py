from django.shortcuts import render, get_object_or_404
from .models import MiniBlog

# Create your views here.

def Blog(request):
    blog = MiniBlog.objects.order_by('-publisTime')[:5]
    return render(request, 'miniBlog/blog.html', {'blog': blog})

def Detail(request, blog_id):
    post = get_object_or_404(MiniBlog, pk=blog_id)
    return render(request, 'miniBlog/detail.html', {'id': blog_id, 'post': post})