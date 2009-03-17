
from setuptools import setup, find_packages
 
setup(
    name='django-cas-provider',
    version='0.1dev',
    description='A "provider" for the Central Authentication Service (http://jasig.org/cas)',
    author='Chris Williams',
    author_email='chris@nitron.org',
    url='http://nitron.org/',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools'],
)
