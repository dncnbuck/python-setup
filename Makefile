.PHONY : clean

all : build/.my-virtual-env/bin/basic-lib

build/.my-virtual-env :
	python3 -m venv build/.my-virtual-env

piplist : install
	build/.my-virtual-env/bin/pip list

build/.my-virtual-env/bin/basic-lib : build/.my-virtual-env
	build/.my-virtual-env/bin/pip install -e basic-lib

build/.my-virtual-env/bin/flake8 : build/.my-virtual-env/bin/basic-lib
	build/.my-virtual-env/bin/pip install flake8

build/.my-virtual-env/bin/coverage : build/.my-virtual-env/bin/basic-lib
	build/.my-virtual-env/bin/pip install coverage

test : build/.my-virtual-env/bin/basic-lib build/.my-virtual-env/bin/flake8 build/.my-virtual-env/bin/coverage
	build/.my-virtual-env/bin/flake8 --max-line-length 120 basic-lib
	build/.my-virtual-env/bin/coverage run -m pytest

clean :
	rm -rf build/