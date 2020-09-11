import json
from .template_engine_model import TemplateEngineModel


class ViewModel:
    def __init__(self, host=None):
        if host:
            self.model = TemplateEngineModel(host)

    # This method checks for the presence of system template in templates collection and inserts if it doesn't exist.
    def insert_system_template(self, template: dict):
        find_response = self.model.find_one_template(template)
        if find_response['status_code'] == 200:
            return {'status_code': 200, 'message': "Customer Template Already Exists."}

        insertion_response = self.model.insert_template(template)
        if insertion_response['status_code'] != 200:
            return {'status_code': insertion_response['status_code'], 'message': "Could not insert system template."}
        else:
            return {'status_code': 200, 'message': "Successfully inserted system template"}

    # This method inserts a created customer template to templates collection.
    def insert_customer_template(self, customer_id: int):
        response = self.model.find_one_template({"customerId": customer_id})
        if response['status_code'] == 200:
            return {'status_code': 200, 'message': "Customer Template Already Exists."}

        sys_te_response = self.model.find_templates({"type": "system"})
        if sys_te_response['status_code'] != 200:
            return {'status_code': sys_te_response['status_code'], 'message': "Could not create customer template."}

        customer_template = self.create_customer_template(sys_te_response['message'], int(customer_id))

        insertion_response = self.model.insert_template(customer_template)
        if insertion_response['status_code'] != 200:
            return {'status_code': insertion_response['status_code'], 'message': "Could not create customer template."}
        else:
            return {'status_code': 200, 'message': "Successfully created customer template"}

    # This method creates a customer template from array of system templates and customer_id
    def create_customer_template(self, system_templates: [], customer_id: int):
        fields = []
        customer_template = {}
        for te in system_templates:
            fields.append(te['fields'])
            customer_template.update(te)

        customer_template['fields'] = fields
        customer_template['customerId'] = int(customer_id)
        customer_template['type'] = 'customer'
        customer_template.pop('_id')

        return customer_template

    # This method finds and returns one customer template with given customer_id if exists.
    def find_customer_template(self, customer_id: int):
        response = self.model.find_one_template({"customerId": customer_id})
        if response['status_code'] == 200:
            response['message'].pop('_id')
            response['message'] = json.dumps(response['message'])

        return response

    # This method deletes all templates in templates collection.
    def delete_all_templates(self):
        return self.model.delete_templates({})
