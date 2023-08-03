from django.db.models import Q
from django.shortcuts import render, redirect

from products.constants import PAGINATION_LIMIT
from products.models import Products, Category, Comment
from products.forms import Category_create, Products_create, CommentsCreateForm


def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':

        shops = Products.objects.all()
        search_text = request.GET.get("search")
        page = int(request.GET.get('page', 1))
        if search_text:
            shops = shops.filter(Q(title__icontains=search_text) |
                                 Q(description__icontains=search_text)
                                 )

        max_page = shops.__len__() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)

        shops = shops[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context_data = {
            'shops': shops,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context_data)


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()

        search_text = request.GET.get("search")

        if search_text:
            category = category.filter(title__icontains=search_text)

            context_data = {'category': category}
            return render(request, 'products/categories.html', context=context_data)


def products_detail_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': CommentsCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Products.objects.get(id=id)
        data = request.POST
        form = CommentsCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                name=form.cleaned_data.get('name'),
                product=product

            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        context_data = {'form': Products}
        return render(request, 'products/', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = Products_create(data, files)
        if form.is_valid():
            Products.objects.create(
                img=form.cleaned_data.get('img'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                category=form.cleaned_data.get('category'),
                prize=form.cleaned_data.get('prize'),
                phone_number=form.cleaned_data.get('phone_number')

            )
            return redirect('/products/')
        return render(request, 'products/categories.html', context={'form': form})


def create_category_view(request):
    if request.method == 'GET':
        context_data = {'form': Category_create}

        return render(request, 'products/categories.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        f = Category_create(data, files)

        if f.is_valid():
            Category.objects.create(
                title=f.cleaned_data.get('title')

            )
            return redirect('/category/')
        return render(request, 'products/categories.html', context={'form': f})
