# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 22
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "isi-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Python language bindings for managing OneFS clusters.",
    maintainer="Isilon SDK",
    maintainer_email="sdk@isilon.com",
    author="Isilon SDK",
    author_email="sdk@isilon.com",
    url="https://github.com/Isilon/isilon_sdk_python",
    keywords=["Swagger", "Isilon SDK", "OneFS", "PowerScale"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="Isilon SDK - Language bindings for the OneFS API",
    project_urls={
        "Source code": "https://github.com/Isilon/isilon_sdk",
        "Documentation": "https://github.com/Isilon/isilon_sdk_python",
    },
    license='MIT',
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=2.7',
)
