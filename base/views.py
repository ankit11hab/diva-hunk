from django.shortcuts import render
from .models import Diva, Hunk, Voter 

# Create your views here.
def home(request):
    divas = Diva.objects.all()
    hunks = Hunk.objects.all()
    context = {
        divas: divas,
        hunks: hunks
    }
    return render(request, 'base/home.html', context)


def divaHunkList(request):
    genderquery = request.GET.get('category') or 'diva'
    searchquery = request.GET.get('search')
    print(genderquery, searchquery)
    return render(request, 'base/list.html')