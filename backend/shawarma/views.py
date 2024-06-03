
from django.shortcuts import render
from .forms import ShawarmaForm
from .forms import MultipleShawarmaForm
from django.forms import formset_factory
from .models import Shawarma
# Create your views here.


def home(request):
    return render(request, "shawarma/home.html")


def order(request):
    # Creating a new "MultipleShawarmaForm" form here "multiple_form = MultipleShawarmaForm()"
    multiple_form = MultipleShawarmaForm()
    if request.method == "POST":
        filled_form = ShawarmaForm(request.POST)
        if filled_form.is_valid():
            # This line is saving the Model Form into the database: "filled_form.save()"
            created_shawarma = filled_form.save()
            # This line is getting the primary key for the created shawarma, "created_shawarma"
            created_shawarma_pk = created_shawarma.id
            note = "Thanks for ordering! Your %s %s and %s shawarma is on its way!" % (filled_form.cleaned_data['size'],
                                                                                       filled_form.cleaned_data['ingredient1'],
                                                                                       filled_form.cleaned_data['ingredient2'],)
            filled_form = ShawarmaForm()
        else:
            created_shawarma_pk = None
            note = "Shawarma has failed. Try again."
        return render(request, "shawarma/order.html", {'created_shawarma_pk': created_shawarma_pk,
                                                       'shawarmaform': filled_form,
                                                       'note': note,
                                                       'multiple_form': multiple_form})

    else:
        form = ShawarmaForm()
        return render(request, "shawarma/order.html", {'shawarmaform': form, 'multiple_form': multiple_form})


def shawarmas(request):
    number_of_shawarmas = 2
    filled_multiple_shawarma_form = MultipleShawarmaForm(request.GET)
    if filled_multiple_shawarma_form.is_valid():
        number_of_shawarmas = filled_multiple_shawarma_form.cleaned_data['number']
    ShawarmaFormSet = formset_factory(ShawarmaForm, extra=number_of_shawarmas)
    formset = ShawarmaFormSet()
    if request.method == 'POST':
        filled_formset = ShawarmaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['ingredient1'])
                print(form.cleaned_data['ingredient2'])
                print(form.cleaned_data['size'])
            note = 'Shawarmas have been ordered!'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'shawarma/shawarmas.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'shawarma/shawarmas.html', {'formset': formset})


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


def blog(request):
    return render(request, "shawarma/blog.html")