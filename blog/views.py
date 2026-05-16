from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "blog/about.html")

def blog(request):
    return render(request, "blog/blog.html")

def blog_detail(request):
    return render(request, "blog/blog_detail.html")