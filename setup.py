from setuptools import setup, find_packages

setup(
    name="mattermost-api-tests",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest==7.4.3",
        "requests==2.31.0",
        "python-dotenv==1.0.0",
        "pytest-html==4.1.1",
        "pytest-reportlog==0.1.2"
    ],
) 