from setuptools import setup, find_packages
from typing import List

HYPHEN_DOT_E="-e ."
def get_requirements(file_path)->List[str]:
    reqs=[]
    with open(file_path) as file_obj:
        reqs=file_obj.readlines()
        reqs=[req.replace("\n","") for req in reqs]
        if HYPHEN_DOT_E in reqs:
            reqs.remove(HYPHEN_DOT_E)
    return reqs



setup(
    name="mypackage",
    version="0.0.1",
    author="Abhinav",
    author_email="abhinavbasa427@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)