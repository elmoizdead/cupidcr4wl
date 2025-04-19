from setuptools import setup, find_packages

setup(
    name="cupidcr4wl",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "cupidcr4wl = cupidcr4wl:main",
        ],
    },
)

