from django.db import models

# Create your models here.
class account(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    sender = models.ForeignKey(account, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(account, on_delete=models.CASCADE, related_name='receiver')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender , " to" , self.receiver