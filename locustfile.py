from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(0.25, 1)
    
    @task
    def hello_world(self):
        self.client.get("http://mockServer:1080/transactions?transactionRef=XVJ3KF9")
