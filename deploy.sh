echo "make dist files"
python setup.py sdist bdist_wheel

echo "upload to pypl"
twine upload dist/*