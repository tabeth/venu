from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import valentine


def index(request):
	# Request the context of the request
	# The context contains information such as the client's machine details
	context = RequestContext(request)

	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template.

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.

	#Foods... This isn't in a model because the model implementation will be a bit a different
	#than what I'm going for at the moment. Eventually this will be deprecated.


	context_dict = {

		'breakfast': valentine.createMenu('Breakfast'),
		'breakfast1': valentine.menu('Breakfast', 1),
		'breakfast2': valentine.menu('Breakfast', 2),
		'breakfast3': valentine.menu('Breakfast', 3),
		'breakfast4': valentine.menu('Breakfast', 4),
		'breakfast5': valentine.menu('Breakfast', 5),
		'breakfast6': valentine.menu('Breakfast', 6),
		'breakfast7': valentine.menu('Breakfast', 7),
		'breakfast8': valentine.menu('Breakfast', 8),
		'breakfast9': valentine.menu('Breakfast', 9),
		'breakfast10': valentine.menu('Breakfast', 10),

		'lunch': valentine.createMenu('Lunch'),
		'lunch1': valentine.menu('Lunch', 1),
		'lunch2': valentine.menu('Lunch', 2),
		'lunch3': valentine.menu('Lunch', 3),
		'lunch4': valentine.menu('Lunch', 4),
		'lunch5': valentine.menu('Lunch', 5),
		'lunch6': valentine.menu('Lunch', 6),
		'lunch7': valentine.menu('Lunch', 7),
		'lunch8': valentine.menu('Lunch', 8),
		'lunch9': valentine.menu('Lunch', 9),
		'lunch10': valentine.menu('Lunch', 10),

		'dinner':  valentine.createMenu('Dinner'),
		'dinner1': valentine.menu('Dinner', 1),
		'dinner2': valentine.menu('Dinner', 2),
		'dinner3': valentine.menu('Dinner', 3),
		'dinner4': valentine.menu('Dinner', 4),
		'dinner5': valentine.menu('Dinner', 5),
		'dinner6': valentine.menu('Dinner', 6),
		'dinner7': valentine.menu('Dinner', 7),
		'dinner8': valentine.menu('Dinner', 8),
		'dinner9': valentine.menu('Dinner', 9),
		'dinner10': valentine.menu('Dinner', 10),
		}

	return render_to_response('valmenu/index.html', context_dict, context)