from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="env4conf",
    version="0.1",
    author="Sven Haardiek",
    author_email="sven@haardiek.de",
    description="Python library to override configuration entries with environment variables",  # noqa 501
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iotec-gmbh/env4conf",
    packages=["env4conf"],
    test_suite="tests",
)
