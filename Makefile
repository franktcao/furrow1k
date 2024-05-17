MY_VAR := $(shell poetry version -s)
BRANCH := 'main'
REMOTE := 'origin'

bump:
	poetry version ${BUMP}
	poetry publish --build
	
	@echo version is ${$@_VERSION}
	$(eval $@_VERSION := $(shell poetry version -s))
	@echo version is ${$@_VERSION}
	git tag ${$@_VERSION} ${BRANCH}
	git push ${REMOTE} tag ${$@_VERSION}
tag:
	# Make sure this runs after bump
	# echo git tag ${VERSION} ${BRANCH}

test:
	# @echo "my var is $(MY_VAR)"
	@echo "my var is $(HAP)"
	$(eval HAP := 1)
	@echo "my var is $(HAP)"
	$(eval HAP := ${eval(${HAP} + 1)})
	@echo "my var is $(HAP)"
	@echo git tag ${VERSION} ${BRANCH}
