import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="samplepack",  # Replace with your own username
    version="0.0.1",
    author="jensqin",
    author_email="jensqin@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jensqin/samplepack",
    packages=setuptools.find_packages(exclude=("tests", "docs")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
