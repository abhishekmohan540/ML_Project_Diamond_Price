from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

#  Reading data from requirements.txt 
def get_requirement(file_path:str)-> List[str]:
    requirements= []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='RegressorProject',
    version='0.0.1',
    author='Abhishek Mohan',
    author_email='abhishekmohan540@gmail.com',
    install_requires= get_requirement('requirements.txt'),
    packages= find_packages()

)