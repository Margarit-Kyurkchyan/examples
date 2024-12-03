from html.parser import HTMLParser
import html5lib
from bs4 import BeautifulSoup
import lxml.html as lh


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1><a href="test.com">asas</body></html>')

document = html5lib.parse("<div><p>Hello World!</div>")
print(document)

html_content = """
<html>
<body>
  <h1>Welcome to My Page</h1>
  <p>Nice to see you.</p>
  <p>If you have any questions or need information on a specific topic, feel free to let me know!</p>
</body>
</html>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extract text from the h1 element
h1_text = soup.find('h1').string
print(h1_text)

# Extract text from all paragraphs
paragraph_texts = [p.get_text() for p in soup.find_all('p')]
print(paragraph_texts)

html_content = """
<html>
<body>
  <h1>Welcome to My Page</h1>
  <p>Nice to see you.</p>
  <p>If you have any questions or need information on a specific topic, feel free to let me know!</p>
</body>
</html>
"""

# Parse the HTML content
tree = lh.fromstring(html_content)

# Extract text from the h1 element
h1_text = tree.xpath('//h1/text()')[0]
print(h1_text)

# Extract text from all paragraphs using XPath
all_paragraph_texts = tree.xpath('//p//text()')
print(all_paragraph_texts)
