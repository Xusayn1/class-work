from django.shortcuts import render

from shared.models import Banner


def home_page_view(request):
    context = {
        'banners': Banner.objects.all().order_by('-id'),
    }
    return render(request, 'index.html', context)


