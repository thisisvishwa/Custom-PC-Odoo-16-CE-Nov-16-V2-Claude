```python
from locust import HttpUser, task, between

class LoadTest(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_product_components(self):
        self.client.get("/product_components")

    @task
    def load_build_configurations(self):
        self.client.get("/build_configurations")

    @task
    def load_compatibility_rules(self):
        self.client.get("/compatibility_rules")

    @task
    def start_custom_pc_configuration_wizard(self):
        self.client.get("/custom_pc_configuration_wizard")

    @task
    def load_sales_order(self):
        self.client.get("/sales_order")

    @task
    def load_invoice(self):
        self.client.get("/invoice")

    @task
    def check_component_availability(self):
        self.client.get("/component_availability_check")

    @task
    def start_custom_pc_production_process(self):
        self.client.get("/custom_pc_production_process")
```