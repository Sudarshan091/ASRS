from setuptools import setup, find_packages

setup(
    name="assrs",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mypy",
        "pytest"
    ],
    author="ASSRS Team",
    description="ASSRS Project Architecture"
)
