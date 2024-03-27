from django.db import models


class Buyer(models.Model):
    first_name = models.CharField(max_length=256)
    second_name = models.CharField(max_length=256)
    phone = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.first_name


class Seller(models.Model):
    first_name = models.CharField(max_length=256)
    second_name = models.CharField(max_length=256)
    phone = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=256)
    date_start_work = models.DateField()
    position = models.CharField(max_length=256, choices=(('Seller', 'Продавец'),
                                                         ('Main Seller', 'Старший продавец'),
                                                         ('Boss', 'Руководитель отдела продаж')))

    def __str__(self):
        return self.first_name


class Product(models.Model):
    product_name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.product_name


class SellsInfo(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sell_date = models.DateTimeField()
    price = models.IntegerField(max_length=20)