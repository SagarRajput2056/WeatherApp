from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    city = ''
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city', '')
        api_key = 'd31ba6844915f7d9baf9e68902f1e4ef'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "City not found"}
    
    return render(request, 'index.html', {'city':city, 'weather_data':weather_data})