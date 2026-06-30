import os

API_SECRET = "sk-test-secret-12345"
DB_PASSWORD = "supersecret"

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def fetch_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return query
