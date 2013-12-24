from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from couchdb import Server
from couchdb import ResourceNotFound
from django.template import RequestContext


SERVER = Server('http://admin:empresadigitala@programs.iriscouch.com/')
if (len(SERVER) == 0):
    SERVER.create('programs')

map_tve1= '''function(doc) {
	if (doc.canal=="tve1")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_clan= '''function(doc) {
	if (doc.canal=="clan")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_tve2= '''function(doc) {
	if (doc.canal=="tve2")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''
	
map_antena3= '''function(doc) {
	if (doc.canal=="antena3")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_neox= '''function(doc) {
	if (doc.canal=="neox")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_nova= '''function(doc) {
	if (doc.canal=="nova")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_cuatro= '''function(doc) {
	if (doc.canal=="cuatro")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_telecinco= '''function(doc) {
	if (doc.canal=="telecinco")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_boing= '''function(doc) {
	if (doc.canal=="boing")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_lasexta= '''function(doc) {
	if (doc.canal=="lasexta")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''

map_lasexta3= '''function(doc) {
	if (doc.canal=="lasexta3")
  		emit(doc._id, (doc.name + " :"+doc.hinicio+"/"+doc.hfin));
}'''


	
 
def index(request):
    programs = SERVER['programs']
    return render_to_response('whatsontv/index.html',{'rows1':programs.query(map_tve1), 
														'rows2':programs.query(map_tve2),
														'rows3':programs.query(map_antena3),
														'rows4':programs.query(map_cuatro),
														'rows5':programs.query(map_telecinco),
														'rows6':programs.query(map_lasexta),
														})

def more(request):
    programs = SERVER['programs']
    return render_to_response('whatsontv/more.html',{'rows1':programs.query(map_tve1), 
														'rows2':programs.query(map_tve2),
														'rows3':programs.query(map_antena3),
														'rows4':programs.query(map_cuatro),
														'rows5':programs.query(map_telecinco),
														'rows6':programs.query(map_lasexta),
														'rowsclan':programs.query(map_clan), 
														'rowsneox':programs.query(map_neox),
														'rowsnova':programs.query(map_nova),
														'rowsboing':programs.query(map_boing),
														'rows63':programs.query(map_lasexta3),
														})												
	
def detail(request,id):	
    programs = SERVER['programs']
    try:
        program = programs[id]
    except ResourceNotFound:
        raise Http404
	map_detail= '''function(doc) {
	if (doc._id==program._id)
  		emit(doc.name, doc.description);
	}'''
    return render_to_response('whatsontv/detail.html',{ 'row':program, }, context_instance = RequestContext(request))
	
def chlist1(request):	
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_tve1), 'imagen':"images/tve.jpg"}, context_instance = RequestContext(request))
		
def chlist2(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_tve2), 'imagen':"images/la2.jpg"}, context_instance = RequestContext(request))

def chlistboing(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_boing), 'imagen':"images/clan.gif"}, context_instance = RequestContext(request))
		
def chlist3(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_antena3), 'imagen':"images/antena3.png"}, context_instance = RequestContext(request))
		
def chlistneox(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_neox), 'imagen':"images/neox.jpg"}, context_instance = RequestContext(request))
		
def chlistnova(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_nova), 'imagen':"images/nova.jpg"}, context_instance = RequestContext(request))
		
def chlist4(request):	
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_cuatro), 'imagen':"images/cuatro.jpg"}, context_instance = RequestContext(request))

def chlist5(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_telecinco), 'imagen':"images/telecinco.jpg"}, context_instance = RequestContext(request))

def chlistboing(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_boing), 'imagen':"images/boing.jpg"}, context_instance = RequestContext(request))

def chlist6(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_lasexta), 'imagen':"images/lasexta.jpg"}, context_instance = RequestContext(request))
	
def chlist63(request):
	programs = SERVER['programs'] 
	return render_to_response('whatsontv/chlist.html',{ 'rows':programs.query(map_lasexta3), 'imagen':"images/lasexta3.jpg"}, context_instance = RequestContext(request))
	
    

