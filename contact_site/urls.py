from django.urls import path
from contact_site import views

"""
URL configuration for the 'contact_site' application, namespaced as 'site'.

Defines the routing paths for all major application functionalities, including:
1. Home: Landing page with "About" and "Services" sections.
2. Contato: Form processing (collection, validation, and email dispatch).
3. Obrigado: Success feedback page after a valid form submission.
"""

app_name = "site"

urlpatterns = [
    path("ACJR/Home", views.Home, name="index"),
    path("ACJR/Contato", views.form_email, name="contato"),
    path("ACJR/Obrigado", views.obrigado, name="obrigado"),
    path("ACJR/Error", views.error_page, name="error"),
]