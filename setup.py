from setuptools import setup, find_packages
setup(
    name='edgegrid-python', 
    version='1.0.7', 
    description='{OPEN} client authentication protocol for python-requests',
    author='Jonathan Landis',
    author_email='jlandis@akamai.com',
    url='https://github.com/akamai-open/AkamaiOPEN-edgegrid-python',
    namespace_packages=['akamai'],
    packages=find_packages(),
    install_requires = [
        'requests>=1.2.2'
        'pyopenssl',
        'ndg-httpsclient',
        'pyasn1',
        'urllib3'
    ],
    license='LICENSE.txt'
)
