import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
     name="sinoj-square-1.0.4",
     version="1.0.8",
     description="It squares the number",
     long_description=README,
     long_description_content_type="text/markdown",
     author="sinoj",
     author_email="sinoj3094@gmail.com",
     license="MIT",
     classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],                              
    packages=["square"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "square=square.__main__:main",
        ]
    },
 )
