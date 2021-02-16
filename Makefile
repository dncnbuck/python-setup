.PHONY : venv install clean

venv :
	python -m venv build/.my-virtual-env

install : venv
	build/.my-virtual-env/bin/pip install requests

piplist : install
	build/.my-virtual-env/bin/pip list

clean :
	rm -rf build/