from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Ticket, TicketPurchase
from .serializers import TicketSerializer, TicketPurchaseSerializer

@api_view(['GET'])
def ticket_list(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ticket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_ticket(request):
    ticket_id = request.data.get("ticket_id")
    quantity = int(request.data.get("quantity", 1))

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if ticket.quantity < quantity:
        return Response({"error": "남은 수량보다 많이 구매할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

    ticket.quantity -= quantity
    ticket.save()

    purchase = TicketPurchase.objects.create(
        ticket=ticket,
        user=request.user,
        quantity=quantity
    )

    serializer = TicketPurchaseSerializer(purchase)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
