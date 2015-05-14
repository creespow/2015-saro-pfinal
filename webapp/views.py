from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def begin(request):
    return render_to_response('begin.html', context_instance=RequestContext(request))

def make_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/private')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/private')
                else:
                    print "No active user"
            else:
                return render_to_response('nouser.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('login.html',{'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def private(request):
    user = request.user
    return render_to_response('private.html', {'user':user}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def make_logout(request):
    logout(request)
    return HttpResponseRedirect('/')