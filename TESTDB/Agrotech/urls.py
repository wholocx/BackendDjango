from django.urls.conf import path
from Agrotech import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', views.logging_in, name = 'login'),
    path('registration', views.registration, name = 'registration'),
    path('arenda_traktor', views.predlojenie1, name = 'arenda_traktor'),
    path('kombArenda', views.kombainiArenda, name= 'kombArenda'),
    path('oprArenda', views.opriskivateliArenda, name= 'oprArenda'),
    path('kombProd', views.kombProd, name= 'kombProd'),
    path('oprProd', views.oprisProd, name= 'oprProd'),
    path('trakProd', views.trakProd, name= 'trakProd'),
    path('user', views.lk, name= 'user'),
    path('user/changeData', views.changeLK, name = 'changeData')
]
