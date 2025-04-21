from django.shortcuts import render
import requests

# Create your views here.
def clz_home(request):
	API_KEY = "c9f53cbe7f968c0114cef95144e91ad4" 
	CITY = 'Lumbini'
	URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
	response = requests.get(URL)
	data = response.json()
	print(data)
	if response.status_code == 200:
		weather_data = {
            "city": CITY,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"],  # Icon for weather condition
        }
	else:
		weather_data = None
	return render(request,'clzhome.html' , {"weather": weather_data})

def clz_location(request):
	API_KEY = "c9f53cbe7f968c0114cef95144e91ad4" 
	CITY = 'Lumbini'
	URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
	response = requests.get(URL)
	data = response.json()
	print(data)
	if response.status_code == 200:
		weather_data = {
            "city": CITY,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"],  # Icon for weather condition
        }
	else:
		weather_data = None
	return render(request,'clzlocation.html' , {"weather": weather_data})

def clz_plantour(request):
	API_KEY = "c9f53cbe7f968c0114cef95144e91ad4" 
	CITY = 'Lumbini'
	URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
	response = requests.get(URL)
	data = response.json()
	print(data)
	if response.status_code == 200:
		weather_data = {
            "city": CITY,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"],  # Icon for weather condition
        }
	else:
		weather_data = None

	return render(request,'clzplantour.html', {"weather": weather_data})

def clz_info(request):
	API_KEY = "c9f53cbe7f968c0114cef95144e91ad4" 
	CITY = 'Lumbini'
	URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
	response = requests.get(URL)
	data = response.json()
	print(data)
	if response.status_code == 200:
		weather_data = {
            "city": CITY,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"],  # Icon for weather condition
        }
	else:
		weather_data = None

	return render(request,'clzinfo.html', {"weather": weather_data} )