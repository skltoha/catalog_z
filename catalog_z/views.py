from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'request': request})


def photo(request):
    return render(request, 'photo-detail.html', {'request': request})


def video(request):
    return render(request, 'videos.html', {'request': request})


def contact(request):
    return render(request, 'contact.html', {'request': request})


def about(request):
    return render(request, 'about.html', {'request': request})


