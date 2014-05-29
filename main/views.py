from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from footballpools.models import FootballPool


def login(request):
	return render(request, 'login.html')

def init_app(request):
	return render(request, 'landing.html')

@login_required
def dashboard(request):
	return render(request, 'app.html', {'username': request.user.username})

@login_required
def equipos(request):
	return render(request, 'equipos.html', {'username': request.user.username})

@login_required
def estadios(request):
	return render(request, 'estadios.html', {'username': request.user.username})

@login_required
def curiosidades(request):
	return render(request, 'curiosidades.html', {'username': request.user.username})

@login_required
def quinielas(request):
	return render(request, 'quiniela.html', {'username': request.user.username})

@login_required
def quinielas_octavos(request):
	return render(request, 'octavos.html', {'username': request.user.username})

@login_required
def quinielas_cuartos(request):
	return render(request, 'cuartos.html', {'username': request.user.username})

@login_required
def quinielas_semis(request):
	return render(request, 'semis.html', {'username': request.user.username})

@login_required
def quinielas_final(request):
	return render(request, 'final.html', {'username': request.user.username})

@login_required
def fase(request):
	return render(request, 'posiciones.html', {'username': request.user.username})

@login_required
def eliminatorias(request):
	return render(request, 'eliminatorias.html', {'username': request.user.username})

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
    return redirect('/')