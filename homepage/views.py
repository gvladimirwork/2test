from django.views.generic import DetailView 
from django.views.generic import ListView
from homepage.models import Item
from homepage.models import Style

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

class ItemList(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'item_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ItemList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['menu'] = Style.objects.all()
        return context

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'item_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['menu'] = Style.objects.all()
        return context

def ajax(request):
	if request.POST.has_key('client_response'):
		x = request.POST['client_response']                 
		y = '123'                       
		response_dict = {}                                         
		response_dict.update({'server_response': y })                                                                  
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		return render_to_response('ajaxexample.html', context_instance=RequestContext(request))