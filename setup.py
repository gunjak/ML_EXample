from setuptools import setup,find_packages
from typing import List
def get_requirements_list()->List[str]:
    """this function return requirements.txt file"""
    with open('requirements.txt') as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name='housing_predictor',
    version='0.1',
    author='gunja',
    description='this is my first project',
    packages=find_packages(),
    install_requires=get_requirements_list()
)

    

