
from django.shortcuts import render
from .forms import ShawarmaForm
from .models import Shawarma
# Create your views here.


def home(request):
    return render(request, "shawarma/home.html")


def order(request):
    if request.method == "POST":
        created_shawarma_pk = None
        filled_form = ShawarmaForm(request.POST)
        if filled_form.is_valid():
            # This line is saving the Model Form into the database: "filled_form.save()"
            created_shawarma = filled_form.save()
            # This line is getting the primary key for the created shawarma, "created_shawarma"
            created_shawarma_pk = created_shawarma.id
            filled_form = ShawarmaForm()
            note = "Thanks for ordering! Your %s %s and %s shawarma is on its way!" % (filled_form.cleaned_data['size'],
                                                                                       filled_form.cleaned_data['ingredient1'],
                                                                                       filled_form.cleaned_data['ingredient2'],)
            filled_form = ShawarmaForm()
        else:
            note = "Shawarma has failed. Try again."
            new_form = ShawarmaForm()
        return render(request, "shawarma/order.html", {'shawarmaform': filled_form,
                                                       'note': note,
                                                       'created_shawarma_pk': created_shawarma_pk
                                                       })

    else:
        form = ShawarmaForm()
        return render(request, "shawarma/order.html", {'shawarmaform': form})


def edit_order(request, pk):
    shawarma = Shawarma.objects.get(pk=pk)
    form = ShawarmaForm(instance=shawarma)
    if request.method == 'POST':
        filled_form = ShawarmaForm(request.POST, instance=shawarma)
        if filled_form.is_valid():
            filled_form.save()
            note = "Order has been updated."
            form = filled_form
            return render(request, 'shawarma/edit_order.html', {'note': note, 'shawarmaform': form, 'shawarma': shawarma})

    return render(request, 'shawarma/edit_order.html', {'shawarmaform': form, 'shawarma': shawarma})


def about(request):
    return render(request, "shawarma/about.html")


def contact(request):
    return render(request, "shawarma/contact.html")
