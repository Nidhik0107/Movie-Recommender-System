from setuptools import setup

with open("readme.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "NIDHI KAINTURA"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'nidhikaintura07@gmail.com',
    description = 'A simple python package to make a simple web app',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO]
    python_requires = '>=3.12',
    install_requires = LIST_OF_REQUIREMENTS,

)