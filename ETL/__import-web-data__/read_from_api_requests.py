#### API requests ###

# Import requests package
import requests

# Assign URL to variable: url
url1 = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r1 = requests.get(url1)
# Decode the JSON data into a dictionary: json_data
json_data1 = r1.json()

# Print each key-value pair in json_data
for k in json_data1.keys():
    print(k + ': ', json_data1[k])

############################################################################################################
# Assign URL to variable: url
url2 = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r2 = requests.get(url2)

# Decode the JSON data into a dictionary: json_data
json_data2 = r2.json()

# Print the Wikipedia page extract
pizza_extract = json_data2['query']['pages']['24768']['extract']
print(pizza_extract)

###########################################################################################################