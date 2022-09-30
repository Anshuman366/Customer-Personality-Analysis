from typing import List
from pkg_resources import Requirement
from setuptools import setup
from typing import List


        

########## DECLARING VARIABLES FOR SETUP FUNCTIONS

PROJECT_NAME='CUSTOMER_PERSONALITY_ANALYSIS'
VERSION='0.0.1'
AUTHOR='Anshuman'
DESCRIPTION='This is the project to analyse the customer personality '
PACKAGES=['Personality_analysis_main']
REQUIREMENT_FILE_NAME='requirements.txt'


def get_requirement_data():
    
    """ This function will return the list of elements present in the 
    requirements.txt file 
    
    """
    with open(REQUIREMENT_FILE_NAME) as file:
        return file.readlines()
        


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirement_data()
)

