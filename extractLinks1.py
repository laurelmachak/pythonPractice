# <a href = "url

page = ' some content text bla bla bla <a href="www.google.com" plus some'#content of a web page stored as a string

start_link = page.find('<a href=')
start_quote = page.find('"',start_link)
end_quote = page.find('"', start_quote+1)
url = page[start_quote+1:end_quote]
print url


