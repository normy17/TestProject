from django.db.models import Max, Min

from web.models import *


def get_report(report_id, data=None):
    match report_id:
        case 0:
            buyers = SellsInfo.objects.filter(seller=data['seller']).values('buyer').distinct()
            lst = []
            for buyer in buyers:
                lst.append(Buyer.objects.get(id=buyer['buyer']))
            return lst
