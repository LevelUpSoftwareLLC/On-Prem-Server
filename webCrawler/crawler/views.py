from django.shortcuts import render
# webCrawler/crawler/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
#@csrf_exempt  # This decorator to exempt this view from CSRF verification
@require_http_methods(["GET"])  # This decorator restricts this view to only handle POST requests
def handle_get(request):
    # Here, you'll define what happens when a POST request is received.
    # For demonstration, let's just return a JSON response saying the request was received.
    response = JsonResponse({'message': 'This is CORS-enabled.'})
    # response['Access-Control-Allow-Origin'] = '*'  # Not recommended for production
    return response
    # data = {"message": "GET request received!"}
    # return JsonResponse(data)

