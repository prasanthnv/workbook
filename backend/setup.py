from setuptools import setup, find_packages

setup(name='workbook', package_dir={'workbook': 'workbook'}, version='0.1', packages=find_packages(
    exclude=['*.tests', '*.tests.*']))
