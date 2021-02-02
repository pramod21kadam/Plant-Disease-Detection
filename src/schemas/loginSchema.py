class loginSchema:
    post = {
    "type": "object",
    "required": [
        "email",
        "password",
        "sign_in"
    ],
    "properties": {
        "email": {
            "$id": "#/properties/email",
            "type": "string",
            "format": "email"
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string"
        },
        "sign_in": {
            "$id": "#/properties/sign_in",
            "type": "boolean"
        }
    }
}