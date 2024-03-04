from mongoengine import connect
connect(db="rptutorials", host="localhost", port=27017)

"""To create a model, you need to subclass Document and provide the required fields as class attributes. 
To continue with the blog example, here’s how you can create a model for your tutorials:"""

from mongoengine import Document, ListField, StringField, URLField

class Tutorial(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True)

"""With this model, you tell MongoEngine that you expect a Tutorial document to have a .title, an .author, a
 list of .contributors, and a .url. The base class, Document, uses that information along with the field 
 types to validate the input data for you."""

tutorial4 = Tutorial(
    title="Beautiful Soup: Build a Web Scraper With Python",
    author="Martin",
    contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
    url="https://realpython.com/beautiful-soup-web-scraper-python/"
)

tutorial4.save()  # Insert the new tutorial

tutorial5 = Tutorial()
tutorial5.title = "Kingsman"
tutorial5.author = "Alex"
tutorial5.contributors = ["Aldren", "Jon", "Joanna"]
tutorial5.url = "https://realpython.com/convert-python-string-to-int/"

tutorial5.save()

for doc in Tutorial.objects:
    print(doc.title)

for doc in Tutorial.objects(author="Alex"):
    print(doc.title)