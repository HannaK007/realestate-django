from django.shortcuts import render, get_object_or_404
from .models import Property
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.

def listings(request):
    properties = Property.objects.all().order_by('-created_at')

    # Filter by location
    location = request.GET.get('location')
    if location:
        properties = properties.filter(location__icontains=location)

    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Filter by bedrooms
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        properties = properties.filter(bedrooms=bedrooms)

    context = {'properties': properties}
    return render(request, 'listings/listings.html', context)

def property_detail(request, slug):
    property = get_object_or_404(Property, slug=slug)
    context = {'property' : property}
    return render(request, 'listings/property_detail.html', context)


def home(request):
    properties = Property.objects.all().order_by('-created_at')

    # Filter by location
    location = request.GET.get('location')
    if location:
        properties = properties.filter(location__icontains=location)

    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Filter by bedrooms
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        properties = properties.filter(bedrooms=bedrooms)

    #Sorting
    sort_by = request.GET.get('sort_by')

    if sort_by == 'price_asc':
        properties = properties.order_by('price')
    elif sort_by == 'price_desc':
        properties = properties.order_by('-price')
    else:  # newest first by default
        properties = properties.order_by('-created_at')

    # Pagination
    paginator = Paginator(properties, 6)  # Show 6 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'page_obj': page_obj}
    return render(request, 'listings/home.html', context)