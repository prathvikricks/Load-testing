from locust import HttpUser, task, between

class LoginUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks
    
    def on_start(self):
        """Login when the test starts"""
        self.login()
    
    def login(self):
        """Perform login with default credentials"""
        response = self.client.post("/login", 
            data={
                "username": "admin",
                "password": "password123"
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        # Verify successful login redirect to dashboard
        if response.status_code != 200 and response.status_code != 302:
            print(f"Login failed with status code: {response.status_code}")
    
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