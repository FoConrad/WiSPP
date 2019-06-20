import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FoConrad",
    version="0.0.1",
    author="Conrad Christensen",
    author_email="conradbchristensen@gmail.com",
    description="Module for adding white space precedence to Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FoConrad/WiSPP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
