from django.shortcuts import render
from Agrotech.models import Customers

def customers(request):
    # cust = Customers.objects.all()
    # for i in cust:
    #     print('******', i.name_cust, i.mail, i.patronymic_cust)
    cust = Customers(surname_cust = 'Сысоев', name_cust = 'Евгений', patronymic_cust = 'Валерьевич', username_cust = 'Valna', mail = '123@gmail.com', pswdhash = '211233123')
    cust.save()
    #Customers.objects.filter(surname_cust = 'Очиров').delete()