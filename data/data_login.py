LOGIN_CREDENTIALS = [
    {
        "name": "valid_login",
        "username": "Iguanabel@gmail.com",
        "password": "Iguanabel",
        "expected": "success"
    },
    {
        "name": "invalid_user",
        "username": "Iguana@gmail.com",
        "password": "Iguanabel",
        "expected": "invalid_credentials",
        "error_message": "Incorrect email or password."
    },
    {
        "name": "empty_username",
        "username": "",
        "password": "Iguanabel",
        "expected": "empty_username",
        "error_message": "Incorrect email or password."
    },
    {
        "name": "invalid_password",
        "username": "Iguanabel@gmail.com",
        "password": "1234",
        "expected": "invalid_credentials",
        "error_message": "Incorrect email or password."
    },
    {
        "name": "empty_password",
        "username": "Iguanabel@gmail.com",
        "password": "",
        "expected": "empty_password",
        "error_message": "Incorrect email or password."
    },
    {
        "name": "empty_fields",
        "username": "",
        "password": "",
        "expected": "empty_username",
        "error_message": "Incorrect email or password."
    }
]