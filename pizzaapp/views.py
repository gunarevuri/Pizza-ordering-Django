from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import PizzaModel, CustomerModel, OrderModel

# Create your views here.

def home(request):
	return render(request, 'pizzaapp/home.html')

def adminloginview(request):
	return render(request, 'pizzaapp/adminlogin.html' )


def adminauthenticateview(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)

	if user is not None and user.username == "gunarevuri":
		login(request, user)
		return redirect('adminhomepage')


	if user is None:
		messages.add_message(request, messages.ERROR, "invalid credencials")
		return redirect('adminloginview')


def adminhomepage(request):
	pizzas = PizzaModel.objects.all()
	context = {
	'pizzas': pizzas
	}
	return render(request, 'pizzaapp/adminhomepage.html', context)


def adminlogout(request):
	logout(request)
	return redirect('adminloginview')

def addpizza(request):

	name = request.POST['pizza']
	price = request.POST['price']
	pizza = PizzaModel(name = name , price = price)
	pizza.save()
	return redirect(adminhomepage)

def deletepizza(request, id):
	pizza = PizzaModel.objects.filter(id = id)
	pizza.delete()
	return redirect(adminhomepage)

def adminorders(request):
	orders = OrderModel.objects.all()
	context = {
		'orders': orders
	}
	return render(request, 'pizzaapp/adminorders.html', context)

def acceptorder(request, pk):
	order = OrderModel.objects.filter(id = pk)[0]
	order.status = "accepted"
	order.save()
	return redirect(adminorders)


def declineorder(request, pk):
	order = OrderModel.objects.filter(id = pk)[0]
	order.status = "declined"
	order.save()
	return redirect(adminorders)



#----customer ---#
def homepageview(request):
	return render(request, "pizzaapp/homepageview.html")

def signupuser(request):
	username = request.POST['username']
	password = request.POST['password']
	phoneno =  request.POST['phoneno']

	# if username already exist 
	if User.objects.filter(username = username).exists():
		messages.add_message(request, messages.ERROR, "user already exist")
		return redirect(homepageview)


	# if username doesnt exist already
	else:
		User.objects.create_user(username = username, password = password).save()
		lastobject = len(User.objects.all()) -1
		CustomerModel( userid = User.objects.all()[lastobject].id, phoneno = phoneno).save()
		messages.add_message(request, messages.ERROR, "user created , Login to create Order")
		return redirect(homepageview)

def userloginview(request):
	return render(request, 'pizzaapp/userlogin.html')

def userauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)
	if user is not None:
		login(request, user)
		return redirect(customerpage)

	if user is None:
		messages.add_message(request, messages.ERROR, "username or password is not correct")
		return redirect(userloginview)

def customerpage(request):
	if not request.user.is_authenticated:
		return redirect(userloginview)
	username = request.user.username
	context = {
		'username': username, 'pizzas': PizzaModel.objects.all()
	}
	return render(request, 'pizzaapp/customerwelcome.html' , context)

def userlogout(request):
	if not request.user.is_authenticated:
		return redirect(userloginview)
	logout(request)
	return redirect(userloginview)

def placeorder(request):
	if not request.user.is_authenticated:
		return redirect(userloginview)
	username = request.user.username
	phoneno = request.POST['phoneno']
	address = request.POST['address']
	ordereditems = ""
	for pizza in PizzaModel.objects.all():
		name = pizza.name
		price = pizza.price
		pizzaid = pizza.id
		qunatity = str( request.POST.get(str(pizzaid),""))
		print(qunatity)
		if str(qunatity) != "0" and str(qunatity) != " ":
			ordereditems = ordereditems + name + " " + str(int(price)*int(qunatity)) +" "+  "qunatity" +" " +qunatity+ " "
	
	print(ordereditems)
	print(phoneno)

	OrderModel(username = username, phoneno =phoneno, address = address , ordereditems = ordereditems).save()
	messages.add_message(request, messages.ERROR, "order successfully placed")
	return redirect(customerpage)

def myorders(request):
	if not request.user.is_authenticated:
		return redirect(userloginview)
	orders = OrderModel.objects.filter(username = request.user.username).all()
	return render(request, 'pizzaapp/myorders.html', {'orders': orders})