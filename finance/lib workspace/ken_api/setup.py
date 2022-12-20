from setuptools import setup
import os

setup(name="tbc_ken_api",
      version='0.3.7',
      description="Trading Bot Club alpaca api",
      author="Kris Luangpenthong",
      author_email="krisken4699@gmail.com",
      url="https://pypi.org/project/tbc-ken-api/",
      install_requires=['requests'],
      packages=['ken_api'],
      package_data={'': ['./README.MD.txt']},
      include_package_data=True,      
      python_requires=">=3.10",
      package_dir={"ken_api":'src'},
      zip_safe=False)
