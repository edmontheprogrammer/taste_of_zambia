from django import forms

from .models import Shawarma, Size


# Note 1: This is creating a form class using the "django forms" approach:
# This is a form class created using "django forms" approach that we imported
# from Django using this line "from django import forms". It allows us to create
# a form add it to "views" ({'shawarmaform': form}) and
# display it on the site using this {{ shawarmaform }}
# class ShawarmaForm(forms.Form):
#     ingredient1 = forms.CharField(
#         label="Ingredient 1", max_length=100, required=False, widget=forms.Textarea)
#     ingredient2 = forms.CharField(
#         label="Ingredient 2", max_length=100, required=False)
#     size = forms.ChoiceField(label="Size", choices=[
#                              ('Small', 'Small'),
#                              ('Medium', 'Medium'),
#                              ('Large', 'Large')])


# Note A: This is creating a from class using model form approach:
# Note B: Advantages of using model form:
#   A. The "model form" approach is more efficient than the "django form" approach
#   B. "model form" mapps directly to the database and stores data that gets send
#       from the web clients or users to our database.
# Note C: "Django form" and "model form" are both inherited from the "forms" class
#     as you can see here ("forms.Form", "forms.ModelForm")
# Note D: Step by Step give for creating "model form":

# Step 1: Create the database model in the "models.py" file
# Step 2: Create the "forms.py" file in the app directory same location as the
#         "models.py" file.
#         import the model class or database model that you created in "models.py" file
#         or that yo want to create the form from For example:
#         " from .models import Shawarma " "
# Step 3: Create the "model form"
#         For example, the code below creates the "model form" for the Shawarma model
# Step 4: Import the model form class in the "views.py" file
#    For example, " from .forms import ShawarmaForm "
#   Then creating the view function where you want to use the model form
#   For example,
# def order(request):
#     if request.method == "POST":
#         filled_form = ShawarmaForm(request.POST)
#         if filled_form.is_valid():
#             note = "Thanks for ordering! Your %s %s and %s shawarma is on its way!" % (filled_form.cleaned_data['size'],
#                                                                                     filled_form.cleaned_data['ingredient1'],
#                                                                                     filled_form.cleaned_data['ingredient2'],)
#             new_form = ShawarmaForm()
#             return render(request, "shawarma/order.html", {'shawarmaform': new_form, 'note': note})
#     else:
#         form = ShawarmaForm()
#         return render(request, "shawarma/order.html", {'shawarmaform': form})
#
# Step 5: Finally, Create the template (html file) where you want to
#       display and show the form to the users and add the form to it.
#
# <h1>Order a Shawarma</h1>

# <h2>{{ note }}</h2>

# <form action="{% url 'order' %}" method="post">
#   {% csrf_token %} {{ shawarmaform }}
#   <input type="submit" value="Order Shawarma" />
# </form>


class ShawarmaForm(forms.ModelForm):

    class Meta:
        model = Shawarma
        # "fields" is used displaying the followling fields from the "Shawarma" model
        # class that we created in the .model file.
        fields = '__all__'
        labels = {
            'ingredient1': 'Ingredient 1',
            'ingredient2': 'Ingredient 2',
            'size': 'Size'
        }
        # "widgets" is used for customizing widgets for the different fields we
        # have in the form fields.
        # widgets = {'size': forms.CheckboxSelectMultiple}


class MultipleShawarmaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
