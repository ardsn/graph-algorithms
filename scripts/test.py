standardize_dictkeys = lambda d: dict((k.lower(), v) for k, v in d.items())

dicio = {}

print(standardize_dictkeys(dicio))