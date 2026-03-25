import requests 

url = "http://andrewbeatty1.pythonanywhere.com/books" 

# Get all book detail
def readbooks(): 

    response = requests.get(url) 
    return response.json()


# Get Specific ID book detail
def readbook(id):     
    geturl = url + "/" + str(id)     
    response = requests.get(geturl)     
    return response.json()

# Create new book 
def createbook(book):    
    print(book)      
    response = requests.post(url, json=book)          
    # should check we have the correct status code     
    return response.json() 

# we could do checking for correct response code here     return response.json() 
bookadd = {"title":"MyFavBook","author":"Akshay Pastagiya","price":"3000"}
if __name__ == "__main__": 
    print (createbook(bookadd))