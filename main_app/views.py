from django.shortcuts import render
from .models import Bag
# from django.http import HttpResponse

# Create your views here.

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
    return render(request, 'bags/detail.html', {'bag': bag})
