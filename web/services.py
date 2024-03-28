from django.db.models import Max, Min, Sum, Count

from web.models import *


def get_report(report_id, data=None):
    match report_id:
        case 0:
            buyers = SellsInfo.objects.filter(seller=data['seller']).values('buyer').distinct()
            lst = []
            for buyer in buyers:
                lst.append(Buyer.objects.get(id=buyer['buyer']))
            return lst
        case 1:
            return SellsInfo.objects.filter(sell_date=data['date']).values()
        case 2:
            sells = SellsInfo.objects.filter(product=data['product']).values('seller').distinct()
            lst = []
            for sell in sells:
                lst.append(Seller.objects.get(id=sell['seller']))
            return lst
        case 3:
            sells = SellsInfo.objects.filter(product=data['product']).values('buyer').distinct()
            lst = []
            for sell in sells:
                lst.append(Buyer.objects.get(id=sell['buyer']))
            return lst
        case 4:
            return SellsInfo.objects.filter(sell_date=data['date']).aggregate(sum=Sum('price'))['sum']
        case 5:
            products = Product.objects.annotate(num_sells=Count('sellsinfo'))
            max_sells = products.aggregate(max=Max('num_sells'))['max']
            return products.get(num_sells=max_sells)
        case 6:
            sellers = Seller.objects.annotate(sum_sells=Sum('sellsinfo__price'))
            max_sum = sellers.aggregate(max=Max('sum_sells'))['max']
            return sellers.get(sum_sells=max_sum)
        case 7:
            buyers = Buyer.objects.annotate(sum_sells=Sum('sellsinfo__price'))
            max_sum = buyers.aggregate(max=Max('sum_sells'))['max']
            return buyers.get(sum_sells=max_sum)
        case 8:
            products = Product.objects.filter(sellsinfo__sell_date__range=(data['first_date'], data['second_date'])).annotate(num_sells=Count('sellsinfo'))
            max_sells = products.aggregate(max=Max('num_sells'))['max']
            return products.get(num_sells=max_sells)
        case 9:
            sellers = Seller.objects.filter(sellsinfo__sell_date__range=(data['first_date'], data['second_date'])).annotate(sum_sells=Sum('sellsinfo__price'))
            max_sum = sellers.aggregate(max=Max('sum_sells'))['max']
            return sellers.get(sum_sells=max_sum)
        case 10:
            buyers = Buyer.objects.filter(sellsinfo__sell_date__range=(data['first_date'], data['second_date'])).annotate(sum_sells=Sum('sellsinfo__price'))
            max_sum = buyers.aggregate(max=Max('sum_sells'))['max']
            return buyers.get(sum_sells=max_sum)