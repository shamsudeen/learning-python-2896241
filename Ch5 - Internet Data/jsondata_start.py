# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request 

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # now we can access the contents of the JSON like any other Python object
    print("The title is: ", theJSON["title"])
    print("The author is: ", theJSON["author"]["name"], " (", theJSON["author"]["email"], ")")

try:
    # Open URL in read mode
    response = urllib.request.urlopen('https://api.example.com/books/1')
except Exception as e:
    print("Error opening URL: ", str(e))
else:
    # Read all data from the URL
    book_data = response.read()
    
    # Decode the byte data using UTF-8 encoding
    textData = book_data.decode("utf-8")
    
    # Process the JSON data
    printResults(textData)  

    
    # output the number of events, plus the magnitude and each event name  

    
    # for each event, print the place where it occurred
    

    # print the events that only have a magnitude greater than 4


    # print only the events where at least 1 person reported feeling something

  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
  

if __name__ == "__main__":
    main()
