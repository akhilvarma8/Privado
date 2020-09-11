import requests
import json

SERVER_URL = 'http://127.0.0.1:8000/te/'


# This method sends a delete request to delete all the templates in the database.
def reset_templates():
    url_endpoint = SERVER_URL + 'reset'
    response = requests.delete(url_endpoint)
    print(response.status_code, response.content)


# This method sends a put request with system templates to insert them into the database.
def put_system_templates():
    url_endpoint = SERVER_URL + 'system/templates'
    system_template_file = open('system_templates.json')
    system_templates = json.load(system_template_file)

    for template in system_templates:
        response = requests.put(url_endpoint, json=template)
        print(response.status_code, response.content)


# This method sends a get request with customer_id to retrieve customer_template.
def get_customer_templates(customer_id):
    url_endpoint = SERVER_URL + 'customer/' + str(customer_id) + '/templates'
    response = requests.get(url_endpoint)
    print(response.status_code, response.content)


# This method sends a post request with customer_id to create customer_template.
def post_customer_templates(customer_id):
    url_endpoint = SERVER_URL + 'customer/' + str(customer_id) + '/templates'
    response = requests.post(url_endpoint)
    print(response.status_code, response.content)


# Run only one function at a time, comment out the rest.
# Run `reset_templates()` before a series of tests to clear the database.
# Run `put_system_templates()` to add system templates to the database.
if __name__ == '__main__':
    reset_templates()
    # put_system_templates()
    # get_customer_templates(10)
    # post_customer_templates(10)
