from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def base(request):
    return render(request, 'home/base.html')


def shop(request):
    return render(request, 'home/shop.html')