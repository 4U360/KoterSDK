import requests, jwt
import urllib.parse
from datetime import datetime, timedelta
import git


class Koter:
    __server = None
    __parser_sv = None
    config = {}
    default_algorithm = "HS512"
    algorithms = (
        "HS256", "HS384", "HS512", "ES256",
        "ES256", "ES384", "ES512", "RS256",
        "RS384", "RS512", "PS256", "PS384",
        "PS512", "EdDSA"
    )
    certificate = None

    def __init__(self, server: str, setup: dict, client_certificate: str = None, client_secret_key: str = None):
        self.__server = server
        self.config = setup

        if client_certificate and client_secret_key:
            self.certificate = (client_certificate, client_secret_key)

    @property
    def server(self):
        if not self.__parser_sv:

            if "http://" not in self.__server and "https://" not in self.__server:
                self.__server = f"https://{self.__server}"

            self.__parser_sv = urllib.parse.urlparse(self.__server)

            if "localhost" not in self.__parser_sv.netloc and "127.0.0.1" not in self.__parser_sv.netloc:
                self.__parser_sv = self.__parser_sv._replace(scheme="https")

        port = f":{self.__parser_sv.port}" if self.__parser_sv.port is not None else ""
        return f"{self.__parser_sv.scheme}://{self.__parser_sv.hostname}{port}"

    def encode(self, data):
        exp = datetime.utcnow() + timedelta(minutes=10)
        payload = {
            "data": data,
            'exp': exp,
            'nbf': datetime.utcnow(),
            'iss': self.config["issuer"],
            'iat': datetime.utcnow() - timedelta(minutes=1),
            "aud": self.config["audience"]
        }

        return jwt.encode(
            payload,
            self.config["secret_key"],
            algorithm=self.config["algorithm"]
        )

    def report(self):
        url = f"{self.server}/sdk/api/install/{self.config['integration_id']}"
        shared = self.encode(self.config.get("shared", {}))
        with requests.post(url, data={
            "shared": shared
        }, cert=self.certificate) as handler:
            handler.raise_for_status()
            return handler

