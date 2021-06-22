from django.contrib import admin
from .models import articles

# Register your models here.

# c1
# admin.site.register(articles)


# c2
@admin.register(articles)
class articleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
