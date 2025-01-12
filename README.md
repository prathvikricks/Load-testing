# Flask Application with Locust Load Testing (Dockerized)

This project demonstrates a simple Flask application with multiple routes and a Locust-based load testing configuration, all containerized using Docker. The Flask app includes basic routes and a login endpoint, while the Locust configuration is designed to test the app's performance.

## Prerequisites

- Docker
- Docker Compose

## Project Structure

Access the services:

Flask App: The Flask application will be accessible at http://localhost:5000/.
Locust UI: The Locust load testing UI will be accessible at http://localhost:8089/.
In the Locust UI:

Set the Target Host to http://flask-app:5000.
Enter the desired number of users and spawn rate.
Click Start Swarming to begin the load test.

**How It Works**


Flask Application (app.py)
The app defines four routes:

/ – Returns "OK".
/about – Returns "It's about.".
/random – Simulates a random delay (0–2 seconds) and returns "It's late.".
/login – A POST route for user authentication, accepting a JSON payload with username and password.
The login is validated against a simple in-memory user database defined as USERS.

Locust Load Testing (locustfile.py)
Test Routes:
Tests the basic /, /about, and /random routes.
Test Login:
Simulates a login POST request using a predefined username and password (test_user and password123).
Docker Compose (docker-compose.yml)
Defines two services:

flask-app – The Flask application, accessible on port 5000.
locust – The Locust load testing service, accessible on port 8089.







When locust Runs i get page showing as

<img width="894" alt="Screenshot 2025-01-12 at 6 51 30 PM" src="https://github.com/user-attachments/assets/e7ce7311-bc91-4d2c-a601-af9b7a77fb04" />

<img width="1467" alt="Screenshot 2025-01-12 at 6 51 52 PM" src="https://github.com/user-attachments/assets/0915bf7b-a716-4147-8bf5-234a183adb59" />

<img width="1470" alt="Screenshot 2025-01-12 at 6 52 31 PM" src="https://github.com/user-attachments/assets/f05e9899-6822-44dc-b57a-c7132d9ef6ee" />

<img width="1470" alt="Screenshot 2025-01-12 at 6 52 44 PM" src="https://github.com/user-attachments/assets/02200053-f48b-4910-8f86-caddd4dc41b2" />


**Finally after performing load testing i can download the report from page it shows the page as below**
<img width="1470" alt="Screenshot 2025-01-12 at 7 03 42 PM" src="https://github.com/user-attachments/assets/a53a170f-3755-4619-a7ba-c86ecc3f875d" />




