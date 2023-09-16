from xml.etree import ElementTree

# Parse an XML file
tree = ElementTree.parse("../../data/input.xml")
root = tree.getroot()

# Access elements and attributes
for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    genre = book.find("genre").text
    price = book.find("price").text
    print(f"Title: {title}, Author: {author}, Genre: {genre}, Price: {price}")
