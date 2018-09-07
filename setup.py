import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecobici",
    version="0.0.1",
    author="Marco Nila",
    author_email="contact.marconila@gmail.com",
    description="This is a python wrapper for the ecobici api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sainoba/ecobici_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
