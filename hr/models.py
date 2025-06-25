from django.db import models

class Payroll(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    amount = models.FloatField()
    month = models.CharField(max_length=10)
    date_paid = models.DateField()

class Leave(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return self.name
