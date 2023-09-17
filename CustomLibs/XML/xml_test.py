import xmltodict

# Read the XML file into a string
with open("../../data/Example.xml", "r") as xml_file:
    xml_data = xml_file.read()

# Parse the XML data into a dictionary
xml_dict = xmltodict.parse(xml_data)

# Access elements and attributes in the dictionary
for book in xml_dict["library"]["book"]:
    title = book["title"]
    author = book["author"]
    genre = book["genre"]
    price = book["price"]
    print(f"Title: {title}, Author: {author}, Genre: {genre}, Price: {price}")