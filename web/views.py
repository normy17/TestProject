from django.shortcuts import render, redirect, get_object_or_404
from web.forms import *
from web.consts import REPORTS_FORM
from web.services import get_report


def add_buyer(request):
    buyers = Buyer.objects.all()
    form = BuyerForm()
    if request.method == 'POST':
        form = BuyerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_buyer')
    return render(request, 'web/add_buyer.html', {'form': form, 'buyers': buyers})


def edit_buyer(request, id):
    buyer = get_object_or_404(Buyer, id=id)
    form = BuyerForm(instance=buyer)
    if request.method == 'POST':
        form = BuyerForm(data=request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            return redirect('add_buyer')
    return render(request, 'web/add_buyer.html', {'form': form})


def add_seller(request):
    sellers = Seller.objects.all()
    form = SellerForm()
    if request.method == 'POST':
        form = SellerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_seller')
    return render(request, 'web/add_seller.html', {'form': form, 'sellers': sellers})


def edit_seller(request, id):
    seller = get_object_or_404(Seller, id=id)
    form = SellerForm(instance=seller)
    if request.method == 'POST':
        form = SellerForm(data=request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('add_seller')
    return render(request, 'web/add_seller.html', {'form': form})


def add_product(request):
    form = ProductForm()
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    return render(request, 'web/add_product.html', {'form': form, 'products': products})


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = SellsForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    return render(request, 'web/add_product.html', {'form': form})


def add_sells(request):
    form = SellsForm()
    sells = SellsInfo.objects.all()
    if request.method == 'POST':
        form = SellsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_sells')
    return render(request, 'web/add_sells.html', {'form': form, 'sells': sells})


def edit_sells(request, id):
    sell = get_object_or_404(SellsInfo, id=id)
    form = SellsForm(instance=sell)
    if request.method == 'POST':
        form = SellsForm(data=request.POST, instance=sell)
        if form.is_valid():
            form.save()
            return redirect('add_sells')
    return render(request, 'web/add_sells.html', {'form': form})


def report_choice(request):
    form = ReportChoice()
    if request.method == 'GET':
        form = ReportChoice(data=request.GET)
        if form.is_valid():
            return redirect('report_choice_2', id=int(form.cleaned_data['choice']))
    return render(request, 'web/report_choice.html', {'form': form})


def report_choice_2(request, id):
    if request.method == 'POST':
        return render(request, 'web/report_choice_2.html', {'form': REPORTS_FORM[id], 'data': get_report(id, request.POST)})
    if REPORTS_FORM[id]:
        return render(request, 'web/report_choice_2.html', {'form': REPORTS_FORM[id]})
    else:
        return render(request, 'web/report_choice_2.html', {'data': get_report(id)})
