"""The PAM Secret Server SDK API facilitates access to the Secret Server
REST API using API key authentication.
Example:

    # connect to Secret Server
    secret_server = SecretServer(base_url, api_key, api_path_uri='/api/v1')
    
    # to get the secret
    secret = secret_server.get_pam_secret(key_here)
"""

import json
from random import random
from AesEverywhere import aes256

import requests

prime=23
genrated=9


class SecretServerError(Exception):
    """An Exception that includes a message and the server response"""

    def __init__(self, message, response=None, *args, **kwargs):
        self.message = message
        super().__init__(*args, **kwargs)


class SecretServerClientError(SecretServerError):
    """An Exception that represents a client error i.e. ``400``."""


class SecretServerServiceError(SecretServerError):
    """An Exception that represents a service error i.e. ``500``."""


class SecretServer:
    """A class that uses an API key to access the Secret Server
    # Diffie hellman
    """

    API_PATH_URI = "/api/v1"

    @staticmethod
    def process(response):
        if response.status_code >= 200 and response.status_code < 300:
            return response
        if response.status_code >= 400 and response.status_code < 500:
            try:
                content = json.loads(response.content)
                if "message" in content:
                    message = content["message"]
                elif "error" in content and isinstance(content["error"], str):
                    message = content["error"]
            except json.JSONDecodeError as err:
                message = err.msg
            raise SecretServerClientError(message, response)
        else:
            raise SecretServerServiceError(response)

    def __init__(
        self,
        base_url,
        api_key,
        api_path_uri=API_PATH_URI,
    ):
        """
        :param base_url: The base URL e.g. ``http://localhost/SecretServer``
        :type base_url: str
        :param api_key: The authorization method to be used
        :type api_key: str
        :param api_path_uri: Defaults to ``/api/v1``
        :type api_path_uri: str
        """

        self.base_url = base_url
        self.api_key = api_key
        self.api_url = f"{base_url}/{api_path_uri.strip('/')}"


    def rand(self):
        return int((random() *10)+1)

    def headers(self, apiKey, publicKeyA, publicKeyB):
        return {
                    'Accept': 'application/json',
                    'User-Agent': 'ENPAST Desktop Client',
                    'Content-Type': 'application/json',
                    'apiKey': apiKey,
                    'publicKeyA': str(publicKeyA),
                    'publicKeyB': str(publicKeyB)
                }
    def get_pam_secret(self, key):
        """Gets a Secret from Secret Server

        :param key: the key of the secret
        :type id: str
        :return: a JSON formatted string representation of the secret
        :rtype: ``str``
        :raise: :class:`SecretServerAccessError` when the caller does not have
                permission to access the secret
        :raise: :class:`SecretServerError` when the REST API call fails for
                any other reason
        """


        privateKeyA=self.rand() 
        privateKeyB=self.rand() 
        publicKeyA = int(pow(genrated,privateKeyA,prime))
        publicKeyB = int(pow(genrated,privateKeyB,prime))

        resp = self.process(
            requests.get(f"{self.api_url}/secretman/GetSecretV2/{key}" ,
            headers=self.headers(self.api_key,publicKeyA,publicKeyB )
            )
        ).text
        
        sharedKeyA = int(pow(int(json.loads(resp)['keyA']),privateKeyA,prime))
        sharedKeyB = int(pow(int(json.loads(resp)['keyB']),privateKeyB,prime))
        finalSec = sharedKeyA ** sharedKeyB
        return aes256.decrypt(json.loads(resp)['value'], str(finalSec)).decode("utf-8")
