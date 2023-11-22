from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

README = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="shared-python-library",  
    version="1.0.0",  
    description=README,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="airtech",
    packages=find_packages(),
    install_requires=["psycop2"],
    classifiers=[
        "Development Status :: 3 - Alpha", 
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="shared, library, postgres ",

    python_requires=">=3.7, <4",
)