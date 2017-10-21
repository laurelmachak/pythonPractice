#procedural abstraction. will make page (now s) the input and url the output 

s = ' some content text bla bla bla <a href="www.google.com" plus some'#content of a web page stored as a string

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return "include this code above your get_next_target() procedure"
        
        
def get_next_target(page):
    start_link= page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote= page.find('"',start_link)
    end_quote= page.find('"', start_quote+1)
    url= page[start_quote+1:end_quote]
    return url, end_quote


def print_all_links(page):
    while True:    
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break
            
#print(print_all_links(get_page("http://xkcd.com/353")))

#print(get_page("http://xkcd.com/353"))