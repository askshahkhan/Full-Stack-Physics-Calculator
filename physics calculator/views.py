from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def calc(request):
    vi = float(request.GET['vi'])
    vf = float(request.GET['vf'])
    time = float(request.GET['time'])
    acc = (vf - vi) / time
    return render(request, 'result.html', {'acceleration':acc})

# def force(request):
#     mass = float(request.GET['mass'])
#     acceleration = float(request.GET['acceleration'])
#     force = mass * acceleration
#     return render (request, 'force_result.html', {'force': force})

# def velocity(request):
#     distance = float(request.GET['distance'])
#     time = float(request.GET['time'])
#     velocity = distance / time

# def pressure(request):
#     force = float(request.GET['force'])
#     area = float(request.GET['area'])
#     pressure = force / area 

# def friction(request):
#     coefficient = float(request.GET['coefficient'])
#     normal = float(request.GET['normal'])
#     friction = float(request.GET['friction'])

# def tension(request):


# def work(request):
#     force = float(request.GET['force'])
#     displacement = float(request.GET['displacement'])
#     work = force * distance / displacement

# def stress(request):
#     area = float(request.GET['area'])
#     force = float(request.GET['force'])
#     stress = force / area

# def torque(request):


# def frequency(request):


# def air_density(request):

# def coulumb(request):
#     charge_1 = float(request.GET['charge_1'])
#     charge_2 = float(request.GET['charge_2'])
#     distance = float(request.GET['distance'])
#     force = ((8.98755 * 10 ^ 9)(charge_1)(charge_2))/(distance)

# def hooke(request):
#     displacement = float(request.GET['spring_displacement'])
#     constant = float(request.GET['spring_constant'])
#     force = -1 * constant * displacement

# def momentum(request):
    
# def gravity(request):


# def horsepower(request):


# # def density(request):
