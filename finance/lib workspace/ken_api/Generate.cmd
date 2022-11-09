python setup.py sdist
pip install .
echo "don't forget to test first"
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*