#__init__.py ko package banaya hai

from setuptools import find_packages, setup
# from typing import List

def get_requirements()->list[str]:
    requirements_list = list[str] = []
    return requirements_list

# python setup.py install  (run krane ke liy)

setup(
    Name = 'sensor',
    version = "0.0.1",
    author = "Shivam",
    author_email = "shrivastavashivam476@gmai.com",
    packages = find_packages(),
    install_requires = get_requirements(), #["pymongo"]

    
)