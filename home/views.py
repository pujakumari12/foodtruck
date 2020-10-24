from django.shortcuts import render
from django.http import HttpResponse
from home.models import FoodTrucks
from django.contrib import messages
import datetime


def adminArea(request):
	return render(request, 'adminArea.html')

def isTruckAvailable(results):
	current = datetime.datetime.now()
	tempObj = []
	for truck in results:
		openTimeHH = truck.open_time.split(":")[0]
		openTimeMM = truck.open_time.split(":")[1]
		
		closeTimeHH = truck.closing_time.split(":")[0]
		closeTimeMM = truck.closing_time.split(":")[1]

		dt_objO = datetime.datetime.strptime((str(current.year)+'.'+str(current.month)+'.'+str(current.day)+' '+ openTimeHH + ':'+ openTimeMM + ':00,00'), ('%Y.%m.%d %H:%M:%S,%f'))
		openTime = dt_objO.timestamp() * 1000
	
		dt_objC = datetime.datetime.strptime((str(current.year)+'.'+str(current.month)+'.'+str(current.day)+ ' '+closeTimeHH + ':'+ closeTimeMM +':00,00'), ('%Y.%m.%d %H:%M:%S,%f'))
		closeTime = dt_objC.timestamp() * 1000

		currentTime = current.timestamp() * 1000
		if (currentTime >= openTime and currentTime <= closeTime):
			tempObj.append({'truck_location':truck.truck_location, 'food_type': truck.food_type, 'is_open': 'open'})
		else:
			tempObj.append({'truck_location':truck.truck_location, 'food_type': truck.food_type, 'is_open': 'closed'})

		return tempObj

def allTrucks(request):
	results1 = FoodTrucks.objects.all()
	data1 = isTruckAvailable(results1)
	print(results1)
	return render(request, 'allTrucks.html', {'allTrucks':data1})


def index(request):
	if request.method == "POST":
		if request.POST.get("searchFood"):
			results = FoodTrucks.objects.all()
			tempObj = []
			for search in results:
				foodItems = search.food_type.split(",")
				for food in foodItems:
					print(request.POST.get("searchFood").lower())
					print(food.lower())
					if request.POST.get("searchFood").lower().strip() == food.lower().strip():
						tempObj.append(search)

			data = isTruckAvailable(tempObj)
			return render(request, 'allTrucks.html', {'allTrucks':data})
		else:
			return render(request, 'home.html')
	else:
		return render(request, 'home.html')

# Create your views here.

def addTruck(request):
	if request.method == "POST":
		if request.POST.get('truckLock') and request.POST.get('foodType') and request.POST.get('openTime') and request.POST.get('closingTime'):
			saveTruck = FoodTrucks()
			saveTruck.truck_location = request.POST.get('truckLock')
			saveTruck.food_type = request.POST.get('foodType')
			saveTruck.open_time = request.POST.get('openTime')
			saveTruck.closing_time = request.POST.get('closingTime')
			saveTruck.save()
			messages.success(request, "The Truck has been added succesfully...!")
			return render(request, 'addTruck.html')
		return render(request, 'addTruck.html')
	else:
		return render(request, 'addTruck.html')
