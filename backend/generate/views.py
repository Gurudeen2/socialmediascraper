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
    
    # login to facebook
    browser.open(url)
    browser.select_form(nr=0)
    browser.form['email'] = "akeem.fatai.3344"
    browser.form['pass'] ="cyberakeem100"
    response = browser.submit()

    # click okay after login 
    browser.open(response.geturl())
    browser.select_form(nr=0)
    res = browser.submit()

    # search people
    searchparam = "Fatai Akeem"
    url = 'https://facebook.com/search_results/?q=Fatai+Akeem'
    browser.open(url)
    browser.find_link(text="See all")
    req=browser.click_link(text="See all")
    page = browser.open(req)
    res = page.read()

    browser.open(page.geturl())
    if browser.find_link(text='See more results'):
        extr_page = urlopen(page.geturl())
        html_bytes = extr_page.read()
        html = html_bytes.decode('utf-8')
        name = html.find('<div class=cf>')
        
    # browser.close()

    # click on see all to extract
    # browser.open()

    # page = urlopen(url)
   
    # page = urlopen(url)
    # html_bytes = page.read()
    # html = html_bytes.decode('utf-8')
    # title = html.find('<title>')
    # # print("itl", title)
    # start_index = title + len('<title')
    # # print("star index", start_index)
    # end_index = html.find('</title>')
    # title = html[start_index:end_index]

    return render(request, 'fb/fb.html', {'title':res})