from django.contrib import admin

# Register your models here.
from .models import Shawarma, Size


admin.site.register(Shawarma)
admin.site.register(Size)
