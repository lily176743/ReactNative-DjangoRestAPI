from django.contrib import admin

# Register your models here.

# Register your models here.
from api.models import Note
from api.Faq import Faq

admin.site.register(Note)
admin.site.register(Faq)
