from setuptools import setup, find_packages

with open("moeda-br/README.md", 'r') as file:
    page_description = file.read()

setup(
    name="moeda-br",
    version="0.0.1",
    author="Lindon Johnson L Macedo",
    description="Conversor de valor float para moeda brasileira",
    long_description=page_description,
    packages=find_packages(),
    python_requires=">=3.5",
) 

