from django.contrib import admin
from django.forms import modelformset_factory

# Register your models here.
from .models import App
@admin.register(App)
class App1(admin.ModelAdmin):
    class Meta():
        model = App
    list_display = ["title","author"]
    search_fields = ['title','author','description']