from django.db import models
from users.models import User

# Create your models here.
class Account(models.Model):
    account_type = models.IntegerField()
    account_number = models.IntegerField()
    account_balance = models.IntegerField()
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_owner')
    is_Main = models.BooleanField(default=False)

    def __str__(self):
        return str(self.account_number)

class Transfer(models.Model):
    # account 1 -> z ktorego sa wysylane
    # account 2-> na ktore sa wysylane
    account1_id = models.IntegerField()
    account2_id = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)