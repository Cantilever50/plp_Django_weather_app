# weather/views.py
from django.shortcuts import render
import requests
from django.conf import settings

def weather(request):
    city = request.GET.get('city', 'New York')  # Default city is New York
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    weather_data = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
    }
    
    return render(request, 'weather/weather.html', {'weather': weather_data})
