bump:
	poetry version ${BUMP}
	poetry publish --build