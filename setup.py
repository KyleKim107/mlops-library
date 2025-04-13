from setuptools import setup

setup(
    name="mlopslib",
    version="0.0.1",
    description="custom library for mlops",
    url="https://github.com/KyleKim107/mlops-library",
    author="kyle",
    packages=["mlopslib"],
    install_requires=[
        "google-cloud-storage==2.6.0"
    ]
)