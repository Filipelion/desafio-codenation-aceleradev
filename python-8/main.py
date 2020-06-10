import jwt

secret = 'acelera'
data = {"language": "Python"}


def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        return jwt.decode(token, secret, algorithms='HS256')

    except jwt.DecodeError:
        return {'error': 2}

token = create_token(data, secret)
verify_signature(token)