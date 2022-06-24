from cmath import e
from django.shortcuts import render, redirect
from .models import Bag, Renter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import RentalsForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# from django.http import HttpResponse

# Create your views here.

# CBV for create bag
class BagCreate(LoginRequiredMixin, CreateView):
    model = Bag
    # fields = '__all__'
    fields = ['name', 'brand', 'colour', 'material', 'cost', 'image']
    # success_url = '/bags/'
    # override CreateViews in built form_valid method to assign the logged in user as the user in the bag model
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form) #invoke the method inherited by the superclass

class BagUpdate(LoginRequiredMixin, UpdateView):
    model = Bag
    fields = '__all__'

class BagDelete(LoginRequiredMixin, DeleteView):
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

@login_required
def bags_index(request):
    # bags = Bag.objects.all()      #removing this so we can display only the bags that belong to the logged in user using the filter method below
    bags = Bag.objects.filter(user=request.user)
    return render(request, 'bags/index.html', {'bags' : bags})

@login_required
def bag_detail(request, bag_id):
    bag = Bag.objects.get(id=bag_id)
    renters_bag_doesnt_have = Renter.objects.exclude(id__in = bag.renters.all().values_list('id'))
    rentals_form = RentalsForm()
    return render(request, 'bags/detail.html', {'bag': bag, 'rentals_form':rentals_form, 'renters' : renters_bag_doesnt_have})

@login_required
def add_rentals(request, bag_id):
    form = RentalsForm(request.POST)
    if form.is_valid():
        new_rental = form.save(commit=False)
        new_rental.bag_id = bag_id
        new_rental.save()
        return redirect('detail', bag_id=bag_id)


class RenterList(LoginRequiredMixin, ListView):
    model = Renter

class RenterDetail(LoginRequiredMixin, DetailView):
    model = Renter

class RenterCreate(LoginRequiredMixin, CreateView):
    model = Renter
    fields = '__all__'

class RenterUpdate(LoginRequiredMixin, UpdateView):
    model = Renter
    fields = '__all__'

class RenterDelete(LoginRequiredMixin, DeleteView):
    model = Renter
    success_url = '/renters/'

@login_required
def assoc_renter(request, bag_id, renter_id):
    Bag.objects.get(id=bag_id).renters.add(renter_id)
    return redirect('detail', bag_id=bag_id)

@login_required
def disassoc_renter(request, bag_id, renter_id):
    Bag.objects.get(id=bag_id).renters.remove(renter_id)
    return redirect('detail', bag_id=bag_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':      #create a user form that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up, please try again.'
    form = UserCreationForm()
    context = {'form' : form, 'error_message' : error_message}
    return render(request, 'registration/signup.html', context)
