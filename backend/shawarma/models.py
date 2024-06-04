from django.db import models

# Create your models here.


# Note 1: You create the different sizes (small, medium and large)
# or choices for the "Size" model in the "admin" site.
# Note 2: Then users will have the "select box" and choices to choose
# "small", "medium" and "large" on the actual site. Also, the administrators or admin
# can create "Shawarma" and choose "Size" from the "admin" site as well.
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Shawarma(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    ingredient1 = models.CharField(max_length=100)
    ingredient2 = models.CharField(max_length=100)
    # Linking the "Shawarma" model to the "Size" model
    # "on_delete=models.CASCADE" relationship is saying that whenever we
    # delete an object from the "Shawarma" ... the system should also delete
    # the object assoicated with it in the "Size" model.
    # In other words, Both objects in the "Shawaram" model and the "Size" model
    # will be removed from the database.
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    special_request = models.CharField(
        max_length=300, null=True, blank=True)

    def __str__(self):
        return self.ingredient1
