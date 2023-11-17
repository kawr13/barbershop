from django.shortcuts import render
from django.views import View


# Create your views here.


class BarberappView(View):

    def get(self, request):
        content = {
            'title': 'BarberShop',
        }
        return render(request, 'barberapp/index.html', context=content)