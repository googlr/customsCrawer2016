from bs4 import BeautifulSoup

file = open("2016may.htm","r")
html_doc = file.read()
#print html_doc

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
#print(soup.get_text())
for td_line in soup.td.children:
    print( td_line )

result = open("2016MayResult.txt", "w")
result.write( soup.get_text().encode('utf-8') )

file.close()
result.close()