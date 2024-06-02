from django import forms

from .models import Shawarma


# Note 1: This is creating a form class using the "django forms" approach:
# This is a form class created using "django forms" approach that we imported
# from Django using this line "from django import forms". It allows us to create
# a form add it to "views" ({'shawarmaform': form}) and
# display it on the site using this {{ shawarmaform }}
# class ShawarmaForm(forms.Form):
#     ingredient1 = forms.CharField(
#         label="Ingredient 1", max_length=100, required=False)
#     ingredient2 = forms.CharField(
#         label="Ingredient 2", max_length=100, required=False)
#     size = forms.ChoiceField(label="Size", choices=[
#                              ('Small', 'Small'),
#                              ('Medium', 'Medium'),
#                              ('Large', 'Large')])


# Note 2: This is creating a from class using model form approach:
# Note 3: Advantages of using model form:
#   A. The "model form" approach is more efficient than the "django form" approach
#   B. "model form" mapps directly to the database and stores data that gets send
#       from the web clients or users to our database.
# Note 3: Step by Step give for creating "model form":
# Step 1: Create the database model in the "models.py" file
# Step 2: Create the "forms.py" file in the app directory same location as the
#         "models.py" file.
#         import the model class or database model that you created in "models.py" file
#         or that yo want to create the form from For example:
#         " from .models import Shawarma " "
# Step 3: Create the "model form"
#         For example, the code below creates the "model form" for the Shawarma model
class ShawarmaForm(forms.ModelForm):
    class Meta:
        model = Shawarma
        # This line is displaying the followling fields from the "Shawarma" model
        # class that we created in the .model file.
        fields = ['ingredient1', 'ingredient2', 'size']
        labels = {
            'ingredient1': 'Ingredient 1',
            'ingredient2': 'Ingredient 2',
            'size': 'Size'
        }
