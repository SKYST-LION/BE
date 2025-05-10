from django.db import models
from django.conf import settings
from performance.models import Performance  # 공연 모델 참조

class Ticket(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name="tickets")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.performance.price

    def __str__(self):
        return f"{self.performance.artist} / ₩{self.price}"

class TicketPurchase(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.ticket.performance.artist} x {self.quantity}"