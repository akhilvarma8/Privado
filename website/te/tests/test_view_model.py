import unittest
from website.te.view_model import ViewModel
import json


# Create your tests here.
class ViewModeTest(unittest.TestCase):
    def setUp(self):
        system_template_file = open('system_templates_input.json')
        self.system_templates = json.load(system_template_file)
        self.view_model = ViewModel()
        system_template_file.close()

    def test_create_customer_template(self):
        customer_template_10 = self.view_model.create_customer_template(self.system_templates, 10)
        customer_template_11 = self.view_model.create_customer_template(self.system_templates, 11)
        customer_template_file = open('customer_template_output.json')
        customer_template_output = json.load(customer_template_file)

        self.assertEqual(customer_template_10, customer_template_output)
        self.assertNotEqual(customer_template_11, customer_template_output)
        customer_template_file.close()


if __name__ == '__main__':
    unittest.main()
