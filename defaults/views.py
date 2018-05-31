from django.shortcuts import render

def defaults_404(request):
    return render(request, 'defaults/404.html')

def defaults_400(request):
    return render(request, 'defaults/404.html')

def defaults_403(request):
    return render(request, 'defaults/404.html')

def defaults_500(request):
    return render(request, 'defaults/404.html')