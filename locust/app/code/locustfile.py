from locust import HttpUser, task, between

class ProjectUser(HttpUser):
    wait_time = between(1, 3)  # Simulate random delays between tasks

    @task
    def test_routes(self):
        self.client.get("/")      # Test the index route
        self.client.get("/about") # Test the about route
        self.client.get("/random") # Test the random route

    @task
    def test_login(self):
        payload = {
            "username": "test_user",
            "password": "password123"
        }
        response = self.client.post("/login", json=payload)
        if response.status_code == 200:
            print("Login successful.")
        else:
            print(f"Login failed with status code {response.status_code}.")
