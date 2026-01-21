"""Setup file for AMC_APIs package."""
from setuptools import setup, find_packages

setup(
    name="AMC_APIs",
    version="0.1.0",
    description="Package for actually installing the attocube python APIs",
    author="djcarrad",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
