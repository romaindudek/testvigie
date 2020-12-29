from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_index(request):
    template_name = "blog/blog_index.html"
    context = {}
    return render(request, template_name, context)