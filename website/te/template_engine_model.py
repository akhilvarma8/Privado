import pymongo
import json


class TemplateEngineModel:
    def __init__(self, host):
        self.client = pymongo.MongoClient(host)
        self.db = self.client.te

    # This method finds all objects in templates collection that conform to the query.
    def find_templates(self, query: dict):
        try:
            templates = self.db.templates.find(query)
        except pymongo.errors.ConnectionFailure:
            return {'status_code': 500, 'message': "Could not connect to database"}
        except pymongo.errors.OperationFailure as e:
            return {'status_code': e.code, 'message': e.details}

        if templates.count() == 0:
            return {'status_code': 404, 'message': "Templates don't exist"}
        else:
            return {'status_code': 200, 'message': templates}

    # This method finds one object in templates collection that conforms to the query.
    def find_one_template(self, query: dict):
        try:
            template = self.db.templates.find_one(query)
        except pymongo.errors.ConnectionFailure:
            return {'status_code': 500, 'message': "Could not connect to database"}
        except pymongo.errors.OperationFailure as e:
            return {'status_code': e.code, 'message': e.details}

        if template is None:
            return {'status_code': 404, 'message': "Template doesn't exist"}
        else:
            return {'status_code': 200, 'message': template}

    # This method inserts the template argument to the templates collection.
    def insert_template(self, template: dict):
        try:
            self.db.templates.insert(template)
        except pymongo.errors.ConnectionFailure:
            return {'status_code': 500, 'message': "Could not connect to database"}
        except pymongo.errors.OperationFailure as e:
            return {'status_code': e.code, 'message': e.details}

        return {'status_code': 200, 'message': "Template successfully inserted"}

    # This method deletes all objects in collection template that conform to the query.
    def delete_templates(self, query: dict):
        try:
            self.db.templates.delete_many(query)
        except pymongo.errors.ConnectionFailure:
            return {'status_code': 500, 'message': "Could not connect to database"}
        except pymongo.errors.OperationFailure as e:
            return {'status_code': e.code, 'message': e.details}

        return {'status_code': 200, 'message': "Templates successfully deleted"}
