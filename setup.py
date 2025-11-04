from setuptools import setup, find_packages

setup(
    name="GITHUB-ACTIONS-TEST",
    version="0.0.1",
    author="Bogoljub Stankovic",
    author_email="bob.stankovic@gov.ab.ca",
    url="https://https://github.com/bstankov/pypi_package_1.git"    description="An application to test python package upload to pypi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    #entry_points={"console_scripts": ["cloudquicklabs1 = src.main:main"]},
    
)