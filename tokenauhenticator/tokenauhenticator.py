import requests
import urllib.parse
import re
from jupyterhub.auth import Authenticator

from tornado import gen
from traitlets import Unicode, Int, Bool, Union, List


class TOKENAuthenticator(Authenticator):
    server_url = Unicode(
        config=True,
        help='URL of CROWD server to contact'
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        token = data['token']

        # call crowd endpoint
        url = urllib.parse.urljoin(self.server_url, token )
        headers = {'Content-Type': 'application/xml',
                   'Accept': 'application/json',
                   'Referrer': self.server_url}
        resp = requests.get(url, data, headers=headers)

        if resp.status_code == 200 && resp.json()['found'] == "true":
            # TODO: return the user name
            return "oo"
        else:
            self.log.warn(resp.text)
            return None
