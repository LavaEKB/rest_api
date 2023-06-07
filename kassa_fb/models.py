from django.db import models

class Credcard(models.Model):
    id = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=80, blank=True, null=True)  # Field name made lowercase.
    clientindex = models.IntegerField(blank=True, null=True)
    limitsum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    canreturn = models.IntegerField(blank=True, null=True)
   
    def __str__(self):
        return self.name


    class Meta:
        managed = False
        db_table = 'CREDCARD'




