from django.contrib import admin

from .models import Novel
from .models import Author

admin.site.register(Novel)
admin.site.register(Author)
