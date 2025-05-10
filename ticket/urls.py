from django.urls import path
from .views import ticket_list, create_ticket, purchase_ticket

urlpatterns = [
    path('', ticket_list, name='ticket_list'),         # GET /api/ticket/
    path('create/', create_ticket, name='ticket_create'), # POST /api/ticket/create/
    path('purchase/', purchase_ticket, name='ticket_purchase')
]