from setuptools import setup
import os
long_description = open(os.path.dirname(__file__)+'/src/README.MD').read()

setup(name="tbc_ken_api",
      version='0.3.2',
      description="Trading Bot Club alpaca api",
      author="Kris Luangpenthong",
      author_email="krisken4699@gmail.com",
      url="https://pypi.org/project/tbc-ken-api/",
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=['requests'],
      packages=['ken_api'],
      python_requires=">=3.10",
      package_dir={"ken_api":'src'},
      zip_safe=False)
