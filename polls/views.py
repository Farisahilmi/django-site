from django.http import HttpResponse

def address_view(request):
    return HttpResponse("Alamat: Jl. Mawar No. 123, Bandung")

def phone_view(request):
    return HttpResponse("Telepon: 0812-3456-7890")
