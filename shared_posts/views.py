from django.shortcuts import render


def index(request):
    return render(request, 'shared_posts/index.html')
