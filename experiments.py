def normalize_url(url):
	first_url = url[:7]
	last_url = url[7:]
	if first_url == "http://":
		str = "https://" + last_url
	else:
		str
	return str

print(normalize_url("http://ya.ru"))