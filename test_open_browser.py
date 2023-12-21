import webbrowser

url = 'https://google.com'
webbrowser.register('firefox',
	None,
	webbrowser.GenericBrowser("/usr/bin/firefox"))
webbrowser.get('firefox').open_new(url)