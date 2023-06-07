from django.db import models

class Sale(models.Model):
    ntab = models.CharField(max_length=10)
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    amcom = models.DecimalField(db_column='AMCOM', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kassid = models.IntegerField(blank=True, null=True)
    sum_gp = models.DecimalField(db_column='SUM_GP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    iactive = models.SmallIntegerField(db_column='IACTIVE', blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fcard = models.IntegerField(blank=True, null=True)
    ncard = models.IntegerField(blank=True, null=True)
    vid = models.IntegerField(db_column='Vid', blank=True, null=True)  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.ntab


    class Meta:
        managed = False
        db_table = 'SALE'
        unique_together = (('ntab', 'id'),)
