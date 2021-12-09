
from django.urls import path
from . import views

urlpatterns = [
    path('get_all_events/', views.get_all_events),
    path('registerForEvent/<int:eventID>/',views.registerForEvent),
    path('get_testimonials/',views.get_testimonials),
    path('get_all_quotes/',views.get_allQuotes),
    path('get_all_resources/',views.get_all_resourcesTable),
    path('get_all_skits/',views.get_all_skits),
    path('register_contact/',views.save_contact_us),




]