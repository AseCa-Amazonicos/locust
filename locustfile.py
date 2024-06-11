from locust import HttpUser, task
import locust

class Customer(HttpUser):
    @task(1)
    def hello(self):
        self.client.post('http://localhost:3001/api/order', json={
            "status":"NOT_STARTED",
            "totalAmount":10,
            "address":"your-home",
            "products":[{
                "productId":3,
                "quantity":5
            },{
                "productId":5,
                "quantity":2
            },{
                "productId":6,
                "quantity":2
            }]
        })

    @task(99)
    def method(self):
        self.client.get("http://localhost:3001/api/stock")

#class ManagingOrders(HttpUser):
#    @task
#    def seeingOrders(self):
#        self.client.get("http://localhost:8080/api/order")


