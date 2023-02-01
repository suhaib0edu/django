from django.http import HttpResponse , JsonResponse
import json
# Create your views here.

def api_home(request,*args,**kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except :
        pass
   # for i in request.headers:
    print(request.headers)
    json.dumps(dict(request.headers))
    data['headers'] = dict(request.headers)
    data['GET'] = dict(request.GET)
    data['POST'] = dict(request.POST)
    return JsonResponse(data)