from setuptools import setup

setup(
    name='jupyterhub-tokenauhenticator',
    version='1.0',
    description='TOKEN Authenticator for JupyterHub',
    url='https://github.com/NCSABrownDog/tokenauthenticator',
    author='Yan Zhao',
    author_email='yanzhao3@illinois.edu',
    license='3 Clause BSD',
    packages=['tokenauhenticator'],
    install_requires=[
        'requests'
    ]
)
