
from django.shortcuts import render, get_object_or_404
from .models import Service

def services_list(request):
    services = Service.objects.all()  # Fetch all services from the database
    return render(request, 'services/services_list.html', {'services': services})

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)  # Fetch service by ID, or 404 if not found
    return render(request, 'services/service_detail.html', {'service': service})

def services(request):
    return render(request, 'service.html')