import setuptools

with open('requirements.txt', 'r') as f:
    loaded_requirements =f.read().splitlines()

setuptools.setup(name='email_script',
                package=['email_script'],
                install_requires=loaded_requirements)