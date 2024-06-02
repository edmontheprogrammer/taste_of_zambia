from django.shortcuts import render
from .forms import ShawarmaForm
# Create your views here.


def home(request):
    return render(request, "shawarma/home.html")


def order(request):
    if request.method == "POST":
        filled_form = ShawarmaForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for ordering! Your %s %s and %s shawarma is on its way!" % (filled_form.cleaned_data['size'],
                                                                                       filled_form.cleaned_data['ingredient1'],
                                                                                       filled_form.cleaned_data['ingredient2'],)
            new_form = ShawarmaForm()
            return render(request, "shawarma/order.html", {'shawarmaform': new_form, 'note': note})
    else:
        form = ShawarmaForm()
        return render(request, "shawarma/order.html", {'shawarmaform': form})
