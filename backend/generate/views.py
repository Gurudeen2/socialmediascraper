from django.shortcuts import render
from urllib.request import urlopen
import mechanize
# Create your views here.

def facebook(request):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11;U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.set_handle_refresh(False)
    url ="https://facebook.com"
    browser.open(url)
    browser.select_form(nr=0)
    browser.form['email'] = "fb username"
    browser.form['pass'] ="fb pass"
    response = browser.submit()
    print("fb res", response.read())

    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    title = html.find('<title>')
    # print("itl", title)
    start_index = title + len('<title')
    # print("star index", start_index)
    end_index = html.find('</title>')
    title = html[start_index:end_index]

    return render(request, 'fb/fb.html', {'title':title})