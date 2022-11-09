from setuptools import setup

setup(name="tbc_hammer",
      version='0.0.1',
      description="Hammer indicator api ",
      author="Kris Luangpenthong",
      author_email="krisken4699@gmail.com",
      url="https://pypi.org/project/tbc-hammer/",
      install_requires=['tbc-ken-api', 'plotly'],
      packages=['tbc_hammer'],
      package_data={'': ['./README.MD.txt']},
      include_package_data=True,
      python_requires=">=3.10",
      package_dir={"tbc_hammer": 'src'},
      zip_safe=False)
