from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="izpy",
        packages=find_packages(include=["izpy_errors", "izpy_requests"]),
        version="0.0.1",
        description="AbstractTest class for generic calls in integration testing of API's",
        author="Izabela Ramos Ferreira",
        install_requires=["requirements"]
    )