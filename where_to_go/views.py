from django.shortcuts import render


def render_main_page(request):
    print('Кто-то зашёл на главную!')
    return render(request, 'index.html')