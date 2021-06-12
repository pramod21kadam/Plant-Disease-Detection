class loginSchema:
    post = {
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": "http://example.com/example.json",
        "type": "object",
        "required": ["email", "password"],
        "properties": {
            "email": {"$id": "#/properties/email", "type": "string", "format": "email"},
            "password": {"$id": "#/properties/password", "type": "string"},
        },
    }
