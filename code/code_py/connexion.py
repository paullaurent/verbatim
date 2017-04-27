from urllib.request import urlopen
html = urlopen("http://127.0.0.1:5000/")
print(html.freq(2,3))