from django import forms

from web.models import *

REPORTS = {
    0: 'Отображение всех покупателей заданного продавца',
    1: 'Отображение всех продаж на заданную дату',
    2: 'Отображение всех продавцов, которые продали заданный товар',
    3: 'Отображение всех покупателей, которые купили заданный товар',
    4: 'Отображение общей суммы продаж в заданный день',
    5: 'Отобразить название самого продаваемого товара',
    6: 'Отобразить лучшего продавца.Критерий определения: максимальная сумма продаж',
    7: 'Отобразить лучшего покупателя. Критерий определения: максимальная сумма покупок',
    8: 'Отобразить название самого продаваемого товара за указанный промежуток времени',
    9: 'Отобразить лучшего продавца. Критерий определения: максимальная сумма продаж за указанный промежуток времени',
    10: 'Отобразить лучшего покупателя. Критерий определения: максимальная сумма покупок за указанный промежуток времени'
}

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ('first_name', 'second_name', 'phone', 'email')


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('first_name', 'second_name', 'phone', 'email', 'date_start_work', 'position')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description')


class SellsForm(forms.ModelForm):
    class Meta:
        model = SellsInfo
        fields = ('buyer', 'seller', 'product', 'sell_date', 'price')


class ReportChoice(forms.Form):
    choice = forms.ChoiceField(
        label='Выберите отчет:',
        choices=zip(REPORTS.keys(), REPORTS.values())
    )


class SellerChoice(forms.Form):
    seller = forms.ChoiceField(
        label='Выберите продавца:',
        choices=((i.id, i) for i in Seller.objects.all())
    )


class ProductChoice(forms.Form):
    product = forms.ChoiceField(
        label='Выберите товар:',
        choices=((i.id, i) for i in Product.objects.all())
    )


class DateChoice(forms.Form):
    date = forms.DateField(
        label='Выберите дату:',
        widget=forms.DateInput(
                attrs={
                    'type': 'date'
                },
            )
    )


class TimeIntervalChoice(forms.Form):
    first_date = forms.DateField(
        label='Выберите дату:',
        widget=forms.DateInput(
                attrs={
                    'type': 'date'
                },
            )
    )
    second_date = forms.DateField(
        label='Выберите дату:',
        widget=forms.DateInput(
                attrs={
                    'type': 'date'
                },
            )
    )
