from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# views.py

class Park:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

# Create a list of Park instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

parks = [
    Park('Yellowstone', 'Wyoming', 'First national park in the U.S.'),
    Park('Yosemite', 'California', 'Known for its waterfalls and granite cliffs.'),
    Park('Grand Canyon', 'Arizona', 'Famous for its immense size and layered bands of color.'),
    Park('Zion', 'Utah', 'Known for its stunning canyons and rock formations.'),
]

def park_index(request):
    return render(request, 'parks/index.html', {'parks': parks})