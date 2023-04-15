"""Module to load test"""
from locust import HttpUser, task, between

class CatsApiUser(HttpUser):
    """ Class to initialize root test"""
    wait_time = between(0.5, 2.5)

    @task
    def root_endpoint(self):
        """tests application home page"""
        self.client.get("")
