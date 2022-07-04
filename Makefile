app_name = api_challenge_bankaya

check:
	@git add .
	@pre-commit

test:
	@pytest -vv
