import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_password(password):
    return len(password) >=6

def required_fields(data, fields):
    return all(field in data and data[field] for field in field)