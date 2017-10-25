from setuptools import setup

setup(
    name='jupyterhub-tokenauthenticator',
    version='1.0',
    description='TOKEN Authenticator for JupyterHub',
    url='https://github.com/NCSABrownDog/tokenauthenticator',
    author='Yan Zhao',
    author_email='yanzhao3@illinois.edu',
    license='3 Clause BSD',
    packages=['tokenauthenticator'],
    install_requires=[
        'requests'
    ]
)
