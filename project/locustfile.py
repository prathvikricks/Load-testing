from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    def on_start(self):
        """Login when the test starts"""
        self.login()
        self.get_token()

    def login(self):
        """Perform login with default credentials"""
        response = self.client.post(
            "/login",
            data={"username": "admin", "password": "password123"},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        if response.status_code == 200 or response.status_code == 302:
            print("Login successful")
        else:
            print(f"Login failed with status code: {response.status_code}")
        
    def get_token(self):
        """Retrieve the token for authenticated requests"""
        response = self.client.get("/token")
        if response.status_code == 200:
            self.token = response.json().get("token")
            if not self.token:
                print("Token not found in response")
        else:
            print(f"Failed to retrieve token with status code: {response.status_code}")
            self.token = None

    @task(3)
    def view_dashboard(self):
        """Access the dashboard page"""
        self.client.get("/dashboard")

    @task(1)
    def logout_and_login(self):
        """Logout and then login again"""
        self.client.get("/logout")
        self.login()

    @task(2)
    def access_login_page(self):
        """Access the login page"""
        self.client.get("/login")
    
    @task(4)
    def access_time_endpoint(self):
        """Access the time endpoint with a valid token"""
        if hasattr(self, 'token') and self.token:
            self.client.get(
                "/time", 
                headers={"x-auth-token": self.token}
            )
        else:
            print("Token not available for accessing /time")

    @task(3)
    def access_random_message_endpoint(self):
        """Access the random message endpoint with a valid token"""
        if hasattr(self, 'token') and self.token:
            self.client.get(
                "/random-message", 
                headers={"x-auth-token": self.token}
            )
        else:
            print("Token not available for accessing /random-message")

    @task(1)
    def refresh_token(self):
        """Fetch a new token"""
        self.get_token()
