from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ProductForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def lista_productos(request):
    products = Product.objects.all()
    if not request.session.get('is_active'):
        return redirect('login')
    return render(request, 'lista_productos.html', {'products': products})

@login_required(login_url='login')
def eliminar_producto(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    if not request.session.get('is_active'):
        return redirect('login')
    return redirect('lista_productos')



@login_required(login_url='login')
def agregar_productos(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductForm()   
    products = Product.objects.all() 
    if not request.session.get('is_active'):
            return redirect('login')
    return render(request, 'agregar_productos.html', {'form': form, 'products': products})

@login_required(login_url='login')
def producto_detalle(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not request.session.get('is_active'):
        return redirect('login')
    return render(request, 'detalle_productos.html', {'product': product})

@login_required(login_url='login')
def carroneitor(request):
    carrito_ids = request.session.get('carrito', [])
    productos_en_carrito = Product.objects.filter(id__in=carrito_ids)
    if not request.session.get('is_active'):
        return redirect('login')
    return render(request, 'carroneitor.html', {'productos_en_carrito': productos_en_carrito})

@login_required(login_url='login')
def sobre_nosotros(request):
    if not request.session.get('is_active'):
        return redirect('login')
    return render(request, 'sobre_nosotros.html')

@login_required(login_url='login')
def agregar_al_carro(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    carrito = request.session.get('carrito', [])
    carrito.append(product.id)
    request.session['carrito'] = carrito
    if not request.session.get('is_active'):
        return redirect('login')
    return redirect('carroneitor')

@login_required(login_url='login')
def reseñas(request):
    reviews = Review.objects.all()
    if not request.session.get('is_active'):
        return redirect('login')
    return render(request, 'reseñas.html', {'reviews': reviews})


@login_required(login_url='login')
def agregar_resena(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not request.session.get('is_active'):
        return redirect('login')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('producto_detalle', pk=product.id)
        if not request.session.get('is_active'):
            return redirect('login')
    else:
        form = ReviewForm()

    return render(request, 'agregar_resena.html', {'form': form, 'product': product})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if not request.session.get('is_active'):
                request.session['is_active'] = True

            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    request.session['is_active'] = False
    return redirect('lista_productos')




@login_required(login_url='login')
def editar_producto(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('producto_detalle', pk=product.id)
    else:
        form = ProductForm(instance=product)

    if not request.session.get('is_active'):
        request.session['is_active'] = True
        
    return render(request, 'editar_producto.html', {'form': form, 'product': product})