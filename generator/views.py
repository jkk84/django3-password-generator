from django.shortcuts import render
import random


# Create your views here.

def home(request):
	return render(request, 'generator/home.html')


def password(request):
	thepassword = ''
	characters = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length', 12))

	if request.GET.get('uppercase') == 'on':
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special') == 'on':
		characters.extend(list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
	if request.GET.get('numbers') == 'on':
		characters.extend(list('0123456789'))

	for x in range(length):
		thepassword += random.choice(characters)

	return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
	return render(request, 'generator/about.html')
