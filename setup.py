from setuptools import find_packages,setup #nb
from typing import List #nb

HYPEN_E_DOT="-e." #nb

def get_requirements(file_path:str)->List[str]:
    '''this fn will return list of reqs'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Advanced Flight Fare Prediction',
    author='dhiyanesh',
    author_email="dhiyanu522@gmail.com",
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)