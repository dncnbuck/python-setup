.PHONY : clean

all : build/.venv/bin/basic-lib

build/.venv :
	python3 -m venv build/.venv

piplist : install
	build/.venv/bin/pip list

build/.venv/bin/basic-lib : build/.venv
	build/.venv/bin/pip install -e basic-lib

build/.venv/bin/flake8 : build/.venv/bin/basic-lib
	build/.venv/bin/pip install flake8

build/.venv/bin/coverage : build/.venv/bin/basic-lib
	build/.venv/bin/pip install coverage


test : build/.venv/bin/basic-lib build/.venv/bin/flake8 build/.venv/bin/coverage
	build/.venv/bin/pip install pytest
	build/.venv/bin/flake8 --max-line-length 120 basic-lib
	build/.venv/bin/coverage run -m pytest

clean :
	rm -rf build/