# The pam Secret Server SDK

The [pam](https://pam.com/) [Secret Server](https://pam.com/products/secret-server/) Python SDK contains classes that interact with Secret Server via the REST API.

## Install

```shell
python -m pip install revbits_ansible
```
## Secret Server

With API key you can authorize the `SecretServer` class to fetch secrets.
### Initializing SecretServer

To instantiate the `SecretServer` class, it requires a `base_url`, `api_key` and an optional `api_path_uri` (defaults to `"/api/v1"`)

```python
from pam.revbits_ansible.server import ServerSecret

secret_server = SecretServer("https://pam.revbits.com", api_key)
```

Secrets can be fetched using the `get_pam_secret` method, which takes a string `key` of the secret and, returns a decoded value :

```python
secret = secret_server.get_pam_secret('DB_HOST')

print(f"secret: {secret}")
```

```shell
from pam.revbits_ansible.server import ServerSecret

secret = ServerSecret(**secret_server.get_pam_secret('DB_HOST'))

DB_HOST = secret
```

## Create a Build Environment (optional)

The SDK requires [Python 3.6](https://www.python.org/downloads/) or higher.

First, ensure Python is in `$PATH`, then run:

```shell
# Clone the repo
git clone https://github.com/RevBits/PAM-ansible-plugin
cd PAM-ansible-plugin

# Create a virtual environment
python -m venv venv
. venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

To build the package, use [Flit](https://flit.readthedocs.io/en/latest/):

```shell
flit build
```
