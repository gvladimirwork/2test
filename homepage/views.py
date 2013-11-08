from django.views.generic import DetailView 
from django.views.generic import ListView
from homepage.models import Item

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

class ItemList(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'item_list.html'

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'item_detail.html'

def ajax(request):
	if request.POST.has_key('client_response'):
		x = request.POST['client_response']                 
		y = '123'                       
		response_dict = {}                                         
		response_dict.update({'server_response': y })                                                                  
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		return render_to_response('ajaxexample.html', context_instance=RequestContext(request))