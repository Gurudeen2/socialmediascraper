from django.shortcuts import render
from urllib.request import urlopen

# Create your views here.

def facebook(request):
    url ="https://facebook.com"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    title = html.find('<title>')
    print("itl", title)
    start_index = title + len('<title')
    print("star index", start_index)
    end_index = html.find('</title>')
    title = html[start_index:end_index]

    return render(request, 'fb/fb.html', {'title':title})