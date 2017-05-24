all:
	python setup.py register
	python setup.py sdist --formats=zip upload
