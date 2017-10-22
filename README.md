# ldapauthenticator
Simple LDAP Authenticator Plugin for JupyterHub

## Installation ##

You can install it from pip with:

```
cd tokenauhenticator 
pip install .
```

## Requirements ##

I've only tested with python3 - anyone willing to test with python2
is welcome to do so! There's no reason it shouldn't work.

## Usage ##

You can enable this authenticator with the folling lines in your
`jupyter_config.py`:

```python
c.JupyterHub.authenticator_class = 'tokenauhenticator.TOKENAuthenticator'
```

### Required configuration ###

At least the following two configuration options must be set before
the LDAP Authenticator can be used:

#### `TOKENAuthenticator.server_url` ####

Address of the TOKEN Server to contact. Just use a bare hostname or IP,
without a port name or protocol prefix.

## Compatibility ##

This has been tested against an OpenLDAP server, with the client
running Python 3.4. Verifications of this code workign well with
other LDAP setups welcome, as are bug reports and patches to make
it work with other LDAP setups!
