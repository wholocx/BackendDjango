# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agrotech(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tech_name = models.CharField(db_column='tech_Name', max_length=40, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    price_period = models.DecimalField(db_column='price_Period', max_digits=19, decimal_places=4)  # Field name made lowercase.
    avlbl_amount = models.IntegerField(db_column='avlbl_Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgroTech'


class Customers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    surname_cust = models.CharField(db_column='Surname_cust', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    name_cust = models.CharField(db_column='Name_cust', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    patronymic_cust = models.CharField(db_column='Patronymic_cust', max_length=20, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    username_cust = models.CharField(db_column='Username_cust', unique=True, max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', unique=True, max_length=40, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    pswdhash = models.CharField(db_column='PswdHash', unique=True, max_length=32, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Rentedtech(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cust = models.ForeignKey(Customers, models.DO_NOTHING, db_column='Cust_id')  # Field name made lowercase.
    tech = models.ForeignKey(Agrotech, models.DO_NOTHING, db_column='Tech_id')  # Field name made lowercase.
    dateofrent = models.DateTimeField(db_column='DateOfRent')  # Field name made lowercase.
    dateofreturn = models.DateTimeField(db_column='DateOfReturn')  # Field name made lowercase.
    amountrented = models.IntegerField(db_column='AmountRented')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RentedTech'


class Techbought(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cust = models.ForeignKey(Customers, models.DO_NOTHING, db_column='Cust_id', blank=True, null=True)  # Field name made lowercase.
    tech = models.ForeignKey(Agrotech, models.DO_NOTHING, db_column='Tech_id', blank=True, null=True)  # Field name made lowercase.
    dateofbuying = models.DateField(db_column='DateOfBuying', blank=True, null=True)  # Field name made lowercase.
    amountbought = models.IntegerField(db_column='AmountBought', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TechBought'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')
    name = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Cyrillic_General_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
