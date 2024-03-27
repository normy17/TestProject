from django.urls import path
from web.views import *

urlpatterns = [
    path('add_buyer/', add_buyer, name='add_buyer'),
    path('add_buyer/<int:id>/', edit_buyer, name='edit_buyer'),
    path('add_seller/', add_seller, name='add_seller'),
    path('edit_seller/<int:id>/', edit_seller, name='edit_seller'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:id>/', edit_product, name='edit_product'),
    path('add_sells/', add_sells, name='add_sells'),
    path('edit_sells/<int:id>/', edit_sells, name='edit_sells'),
    path('reports/', report_choice, name='report_choice'),
    path('reports2/<int:id>/', report_choice_2, name='report_choice_2')
]
