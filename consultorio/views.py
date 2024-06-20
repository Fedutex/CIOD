from django.shortcuts import render


def consultorio(request):
    return render(request, 'consultorio/home.html', {})
