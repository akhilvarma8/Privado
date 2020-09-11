from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .view_model import ViewModel

file = open('config.json')
view_model = ViewModel(host=json.load(file)["mongo_host"])
file.close()


@csrf_exempt
def reset_templates(request):
    if request.method == "DELETE":
        response = view_model.delete_all_templates()
    else:
        response = {'status_code': 404, "message": "Endpoint doesn't exist"}

    return create_http_response(response)


@csrf_exempt
def system_templates(request):
    if request.method == "PUT":
        template = json.loads(request.body)
        response = view_model.insert_system_template(template)
    else:
        response = {'status_code': 404, "message": "Endpoint doesn't exist"}

    return create_http_response(response)


@csrf_exempt
def customer_templates(request, customer_id):
    if not customer_id.isdigit():
        return create_http_response({'status_code': 400, "message": "customer_id needs to be numeric"})

    if request.method == "GET":
        response = view_model.find_customer_template(int(customer_id))
    elif request.method == "POST":
        response = view_model.insert_customer_template(int(customer_id))
    else:
        response = {'status_code': 404, "message": "Endpoint doesn't exist"}

    return create_http_response(response)


def create_http_response(response: dict):
    http_response = HttpResponse()
    http_response.status_code = response['status_code']
    http_response.content = response['message']
    return http_response
