VERSION := $(shell poetry version | grep -oE '[^ ]+$$')

.PHONY: all list clean docs publish version

all: list

list:
	@sh -c "$(MAKE) -p no_targets__ | \
		awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {\
			split(\$$1,A,/ /);for(i in A)print A[i]\
		}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"

clean:
	rm -rf build/ dist/ **/__pycache__/
	rm -f *.spec **/*.pyc

build: clean
	@poetry build

docs: build
	@poetry run mkdocs build --clean

publish: clean build docs
	@mkdocs gh-deploy
	@poetry publish

version:
	@echo $(VERSION)
