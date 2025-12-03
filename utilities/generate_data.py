"""
Test data generator using Faker
"""
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()


class EmployeeDataGenerator:
    """Generate employee test data"""

    @staticmethod
    def generate_employee():
        """Generate random employee data"""
        return {
            "firstName": fake.first_name(),
            "middleName": fake.first_name(),
            "lastName": fake.last_name(),
            "employeeId": f"EMP{random.randint(1000, 9999)}",
            "email": fake.email(),
            "phone": fake.phone_number()[:15],
            "dateOfBirth": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d"),
            "nationality": random.choice(["Egyptian", "American", "British", "Canadian"]),
            "maritalStatus": random.choice(["Single", "Married", "Divorced"]),
            "gender": random.choice(["Male", "Female"])
        }

    @staticmethod
    def generate_multiple_employees(count: int = 5):
        """Generate multiple employees"""
        return [EmployeeDataGenerator.generate_employee() for _ in range(count)]


class UserDataGenerator:
    """Generate user test data"""

    @staticmethod
    def generate_user():
        """Generate random user data"""
        return {
            "username": fake.user_name()[:20],
            "password": fake.password(length=12),
            "employeeName": fake.name(),
            "userRole": random.choice(["Admin", "ESS"]),
            "status": random.choice(["Enabled", "Disabled"])
        }

    @staticmethod
    def generate_credentials():
        """Generate login credentials"""
        return {
            "username": fake.user_name()[:20],
            "password": fake.password(length=12)
        }


class LeaveDataGenerator:
    """Generate leave request data"""

    @staticmethod
    def generate_leave_request():
        """Generate random leave request"""
        start_date = fake.date_between(start_date='+1d', end_date='+30d')
        end_date = start_date + timedelta(days=random.randint(1, 10))

        return {
            "leaveType": random.choice(["Casual Leave", "Sick Leave", "Annual Leave"]),
            "fromDate": start_date.strftime("%Y-%m-%d"),
            "toDate": end_date.strftime("%Y-%m-%d"),
            "comment": fake.sentence(),
            "duration": random.choice(["Full Day", "Half Day"])
        }


# Test the generators
if __name__ == "__main__":
    print("Employee Data:")
    print(EmployeeDataGenerator.generate_employee())
    print("\nUser Data:")
    print(UserDataGenerator.generate_user())
    print("\nLeave Request:")
    print(LeaveDataGenerator.generate_leave_request())