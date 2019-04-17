import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sma-web-parser",
    version="0.0.1",
    author="Moritz Krautwald",
    author_email="moritz.krautwald@outlook.de",
    description="sma-web-interface parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mo-pyy/sma-web-parser",
    py_modules=['sma'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)