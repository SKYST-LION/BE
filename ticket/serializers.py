from rest_framework import serializers
from .models import Ticket, TicketPurchase

class TicketSerializer(serializers.ModelSerializer):
    performance = serializers.StringRelatedField()  # 공연 제목 표시용
    class Meta:
        model = Ticket
        fields = ['id', 'performance', 'quantity', 'created_at']

class TicketPurchaseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    ticket = TicketSerializer(read_only=True)

    class Meta:
        model = TicketPurchase
        fields = ['id', 'user', 'ticket', 'quantity', 'purchased_at']
