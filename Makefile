.PHONY : venv install clean piplist basic

venv :
	python3 -m venv build/.my-virtual-env

install : venv
	build/.my-virtual-env/bin/pip install requests

piplist : install
	build/.my-virtual-env/bin/pip list

basic-lib : install
	build/.my-virtual-env/bin/pip install -e basic-lib

flake8 : basic-lib
	build/.my-virtual-env/bin/pip install flake8

coverage : basic coverage
	build/.my-virtual-env/bin/pip install coverage

test : basic flake8 coverage
	build/.my-virtual-env/bin/flake8 --max-line-length 120 basic-lib
	build/.my-virtual-env/bin/coverage run -m pytest

clean :
	rm -rf build/