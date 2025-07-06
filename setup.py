'''
The setup.py file is an essential part of packaging and distributing Python projects. It is used by setup tools (or disutils in older python version) to define the configuration of your project, such as its metadata, dependencies and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
  requirement_lst:List[str]=[]
  try:
    with open('requirement.txt', 'r')as file:
      lines = file.readlines()

      for line in lines:
        requirement = line.strip()
        if requirement in requirement != '-e .':
          requirement_lst.append(requirement)

  except FileNotFoundError:
    print("Requirement.txt file is not found")

  return requirement_lst

setup(
  name="NetworkSecurity",
  version="0.0.1",
  author="SujeetKumar",
  author_email="sujeetkumarak40@gmail.com",
  packages=find_packages(),
  install_requires=get_requirement()
)

