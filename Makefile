MY_VAR := $(shell poetry version -s)
BRANCH := 'main'
REMOTE := 'origin'

bump:
	poetry version ${BUMP}
	poetry publish --build
	$(eval VERSION := $(shell poetry version -s))
	git tag ${VERSION} ${BRANCH}
	git push ${REMOTE} tag ${VERSION}
tag:
	# Make sure this runs after bump
	# echo git tag ${VERSION} ${BRANCH}

test:
	$(eval VERSION := $(shell poetry version -s))
	@echo "my var is $(MY_VAR)"
	@echo git tag ${VERSION} ${BRANCH}
