from django.shortcuts import render, redirect
from .models import Bag
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RentalsForm



# from django.http import HttpResponse

# Create your views here.

# CBV for create bag
class BagCreate(CreateView):
    model = Bag
    fields = '__all__'
    # success_url = '/bags/'

class BagUpdate(UpdateView):
    model = Bag
    fields = '__all__'

class BagDelete(DeleteView):
    model = Bag
    success_url = '/bags/'

# class Bag:
#     def __init__(self, name, brand, colour, material, cost):
#         self.name = name
#         self.brand = brand
#         self.colour = colour
#         self.material = material
#         self.cost = cost

# bags = [
#     Bag('The Trine', 'Bottega Veneta', 'Ice', 'Leather', 900),
#     Bag('Dionysus', 'Gucci', 'Red and Pink', 'Leather', 789),
#     Bag('By The Way', 'Fendi', 'Green', 'Leather', 1450)
# ]



# defining the home view
def home(request):
    # return HttpResponse('<h1> Bag Collector Homepage </h1>')
    return render(request, 'home.html')

# defining the about page
def about(request):
    return render(request, 'about.html')

def bags_index(request):
    bags = Bag.objects.all()
    return render(request, 'bags/index.html', {'bags' : bags})

def bag_detail(request, bag_id):
    bag = Bag.objects.get(id=bag_id)
    rentals_form = RentalsForm()
    return render(request, 'bags/detail.html', {'bag': bag, 'rentals_form':rentals_form})

def add_rentals(request, bag_id):
    form = RentalsForm(request.POST)
    if form.is_valid():
        new_rental = form.save(commit=False)
        new_rental.bag_id = bag_id
        new_rental.save()
        return redirect('detail', bag_id=bag_id)