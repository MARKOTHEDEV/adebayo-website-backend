from django.contrib import admin
from .models import (
    User,peopleEnrollfor,Event,Testimonial, Quotes,ResourcesTable,SkitTable
)

admin.site.register(User)
admin.site.register(peopleEnrollfor)
admin.site.register(Event)
admin.site.register(Testimonial)
admin.site.register(ResourcesTable)
admin.site.register(SkitTable)