from django.contrib import admin

# Register your models here.
from .models import Animation

@admin.register(Animation)
class Animation(admin.ModelAdmin):
    # Customize your admin panel here
    list_display = ['character','mode','emotion','background']
