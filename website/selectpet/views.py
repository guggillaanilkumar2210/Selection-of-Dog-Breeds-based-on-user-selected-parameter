from django.shortcuts import render, get_list_or_404
from .models import Pet
# Create your views here.
def index(request):
    return render(request, 'selectpet/index.html')

def resp(request):
    pet_objects = get_list_or_404(Pet, size = request.POST['size'], hair=request.POST['length'])

    return render(request, 'selectpet/resp.html', {'pets':pet_objects})