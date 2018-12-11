#!/usr/bin/env python
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="gitlab_job_exporter",
    version="0.0.1",
    author="Sven Hertzberg",
    author_email="sven.hertzberg@cloudcentric.de",
    description="Package to scrape running_time, duration_time, status, etc. of Gitlab jobs using prometheus time series format",
    license='MIT',
    long_description=readme(),
    url="https://gitlab.codecentric.de/cloudcentric/openstack-gitlab-runner",
    include_package_data = True,
    scripts=['bin/gitlab_job_exporter'],
    packages=find_packages(),
    install_requires=[
        'prometheus_client',
        'python-dateutil',
        'urllib3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
