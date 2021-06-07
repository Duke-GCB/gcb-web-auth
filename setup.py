import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='gcb-web-auth',
    version='1.1.3',
    packages=find_packages(),
    install_requires=[
        'DukeDSClient>=3.0.0',
        'PyJWT==1.5.2',
        'requests>=2.20.0',
        'requests-oauthlib==0.8.0',
        'djangorestframework-jwt==1.11.0',
    ],
    include_package_data=True,
    license='MIT License',
    description='Django app to integrate Duke OAuth for use in GCB.'
)
