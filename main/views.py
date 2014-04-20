from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from footballpools.models import FootballPool


def enter(request):
	return render(request, 'login.html')


@login_required
def home(request):
	return render(request, 'index.html', {'username': request.user.username})

@login_required
def test_quiniela(request):
	social = request.user.social_auth
	#print(social.get(provider='facebook').extra_data['birthday'])
	#profile = get_user()
	#print(profile)
	return render(request, 'test.html', {'username': request.user.username})	



def log_out(request):
    logout(request)
    return redirect('enter')