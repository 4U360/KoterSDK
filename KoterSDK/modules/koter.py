import jwt
from django.utils.timezone import datetime, timedelta
from django.conf import settings


class Koter:
    server = settings.KOTER_SERVER_URL

    def encode(self, data):
        exp = datetime.utcnow() + timedelta(**settings.KOTER_EXPIRES)
        payload = {
            "data": data,
            'exp': exp,
            'nbf': datetime.utcnow(),
            'iss': settings.KOTER_ISSUER,
            'iat': datetime.utcnow() - timedelta(minutes=1),
            "aud": settings.KOTER_AUDIENCE
        }

        return jwt.encode(
            payload,
            settings.KOTER_SECRET_KEY,
            algorithm=settings.KOTER_ALGORITHM,
        )

    def decode(self, encoded):
        return jwt.decode(encoded, key=settings.KOTER_SECRET_KEY, options={
            "require": ["exp", "nbf", 'iss', 'iat', 'aud']
        }, audience=settings.KOTER_ISSUER, issuer=settings.KOTER_AUDIENCE, algorithms=[settings.KOTER_ALGORITHM])
