from django.contrib import admin

# Register your models here.
from .models import Contact,Home1,Home2,Firm
admin.site.register(Contact)
admin.site.register(Home1)
admin.site.register(Home2)
admin.site.register(Firm)
