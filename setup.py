import setuptools

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name="gutools", # Replace with your own username
    version="0.0.1",
    author="GUSEC",
    author_email="gusecurity@protonmail.com",
    description="Python package with useful tools to assist with CTF challenges",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/gusecurity/gutools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)