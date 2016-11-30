from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/index02.html', {})

# Create your views here.
