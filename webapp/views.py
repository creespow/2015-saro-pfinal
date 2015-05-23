from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, date, time, timedelta
from models import event, user_choices, choice
from webapp import xml_parser
from .forms import RefreshButton, Filter, PickButton

# Create your views here.

def parser(request):    
    try:
        #Delete previous DB content        
        #event.objects.all().delete()
        xml_parser.parse_it()
    except:
        #Parse XML and create new DB content
        xml_parser.parse_it()

    return HttpResponseRedirect('/todas')

def begin(request):
    user = request.user
    ##check
    if user.is_authenticated():
        users = user_choices.objects.filter(user=user)
        nameuser = False
        for row in users:
            if row.user == user:
                nameuser = True
        if nameuser:
            name = user_choices(user=user)
            name.save()
    ##check
    events_lst = event.objects.order_by("date")
    out = ''
    for count in range(10):
        out += "<div class='block'>"
        out += "<hr>"
        out += "<h3>" + "<u>" + events_lst[count].title + "</u>" + "</h3>"
        out += "<br>" + "Precio: " + events_lst[count].price + "</br>"
        out += "<br>" + "Larga duracion: " + str(events_lst[count].long_duration) + "</br>"
        out += "<br>" + "Fecha: " + events_lst[count].date + "</br>"
        out += "<br>" + "Hora: " + events_lst[count].time + "</br>"        
        out += "<br>" + "Lugar: " + events_lst[count].place + "</br>"
        out += "<br>" + "Tipo de evento: " + events_lst[count].event_type+ "</br>"
        out += "<br><a href=" + events_lst[count].url + ">" + "Mas info" + "</a></br>"
        out += "</div>"
    if request.user.is_authenticated():        
        return render_to_response('beginauth.html', {'user':user, 'out':out}, context_instance=RequestContext(request))
    else:
        return render_to_response('begin.html', {'out':out}, context_instance=RequestContext(request))

def help(request):
    user = request.user
    if request.user.is_authenticated():        
        return render_to_response('helpauth.html', {'user':user}, context_instance=RequestContext(request))
    else:
        return render_to_response('help.html', context_instance=RequestContext(request))

def make_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print "No active user"
            else:
                return render_to_response('nouser.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('login.html',{'form':form}, context_instance=RequestContext(request))

def save(request, event_id):
    user = request.user
    username = user_choices.objects.get(user=user)
    print username
    today = str(date.today())
    print today
    ident = int(event_id)
    print ident
    content = event.objects.get(id=ident)    
    try:
        c = choice (conten=content, username = username, choose_date = today)
        c.save()
    except:
        print "except"
    
    return HttpResponseRedirect("/todas")

def all(request):
    
    user = request.user  
    if request.method == 'POST':
        event_lst = event.objects.all()
        filtertitle  = request.POST.get("title")               
        if filtertitle:
            event_lst = event.objects.filter(title=filtertitle)            
        filterprice = request.POST.get("price")
        if filterprice:
            event_lst = event.objects.filter(price=filterprice)
        filterdate = request.POST.get("date")
        if filterdate:
            event_lst = event.objects.filter(date=filterdate)
        #if RefreshButton(request.POST):    
        #    refresh = RefreshButton(request.POST)
        #    return HttpResponseRedirect('/makeparse/')        
    else:
        event_lst = event.objects.all()
    
    out = ""    
    for row in event_lst:
        out += "<div class='block'>"
        out += "<hr>"
        out += "<h3>" + "<u>" + row.title + "</u>" + "</h3>"
        out += "<br>" + "Precio: " + row.price + "</br>"
        out += "<br>" + "Larga duracion: " + str(row.long_duration) + "</br>"
        out += "<br>" + "Fecha: " + row.date + "</br>"
        out += "<br>" + "Hora: " + row.time + "</br>"        
        out += "<br>" + "Lugar: " + row.place + "</br>"
        out += "<br>" + "Tipo de evento: " + row.event_type+ "</br>"
        out += "<br><a href=" + row.url + ">" + "Mas info" + "</a></br>"
        out += "</div>"
        if request.user.is_authenticated():
            out += "<br>" + '<form action= "/save/' + str(row.id) + '"method="GET">' +\
                 '<input id="guardar" class="myButton2" type="submit" value="Guardar en favoritos"></form>' + "</br>"
        
    button = RefreshButton()

    if request.user.is_authenticated():        
        return render_to_response('todasauth.html',{'out':out, 'form':button}, context_instance=RequestContext(request))
    else:
        return render_to_response('todas.html', {'out':out, 'form':button}, context_instance=RequestContext(request))

def userpage(request, username):

    username = user_choices.objects.get(user=username)

    event_lst = username.selected_event.all()
    out=""
    for row in event_lst:
        out += "<div class='block'>"
        out += "<hr>"
        out += "<h3>" + "<u>" + row.title + "</u>" + "</h3>"
        out += "<br>" + "Precio: " + row.price + "</br>"
        out += "<br>" + "Larga duracion: " + str(row.long_duration) + "</br>"
        out += "<br>" + "Fecha: " + row.date + "</br>"
        out += "<br>" + "Hora: " + row.time + "</br>"        
        out += "<br>" + "Lugar: " + row.place + "</br>"
        out += "<br>" + "Tipo de evento: " + row.event_type+ "</br>"
        out += "<br><a href=" + row.url + ">" + "Mas info" + "</a></br>"
        out += "</div>"

        select = choice.objects.get(conten=row, username=username)
        choose_date = select.choose_date

        out += "<br>" + "Elegida el dia: " + str(choose_date) + "</br>"

    if request.user.is_authenticated():        
        return render_to_response('userpageauth.html',{'out':out}, context_instance=RequestContext(request))
    else:
        return render_to_response('userpage.html', {'out':out}, context_instance=RequestContext(request))

def get_rss(request, username):
    username = user_choices.objects.get(user=username)

    event_lst = username.selected_event.all()
    out = '<?xml version="1.0" encoding="ISO-8859-1" ?>\n' + \
        '<rss version="2.0">\n' + \
        '\t<channel>\n' + \
        '\t\t<title>RSS"</title>\n'
    for row in event_lst:
        out += '\t<item>\n'
        out += '\t\t<Title>' + row.title + '</Title>\n'
        out += '\t\t<Price>' + row.price + '</Price>\n'
        out += '\t\t<Long_duration>' + str(row.long_duration) + '</Long_duration>\n'
        out += '\t\t<Date>' + row.date + '</Date>\n'
        out += '\t\t<Time>' + row.time + '</Time>\n'
        out += '\t\t<Type>' + row.event_type + '</Type>\n'
        out += '\t</item>'        
    
    return HttpResponse (out + '\t</channel>\n</rss>\n', content_type = "rss")
    

@login_required(login_url='/login')
def private(request):
    user = request.user    
    return render_to_response('private.html', {'user':user}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def make_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



