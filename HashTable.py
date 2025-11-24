import csv
import time

#Author: Steven Harrington
#Date: 11/23/2025
#How techniques work
    #Mid-square function
        #takes in a string
        #makes a integer to keep track of the sum of characters
        #go through each character in the string, and converts to unicode value
        #it adds this to the sum
        #squares the sum and makes a string
        #slices the middle chunk of the string and makes an integer
        #returns the remainder of the integer divided by 997

    #Add/linear probing by prime number collision
        #attempts to add at the index it recieved from the hash function
        #if there is something there then, it go forward 19 spots
        #if this is bigger than the size of the table, then it extends appropiately
        #it then places it at that index



class DataItem:
    #makes a dataItem with the different info and takes off appropiate symbols
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_data = line[2]
        self.director = line[3]
        self.revenue = line[4][1:]
        self.rating = line[5]
        self.min_duration = line[6]
        self.production_company = line[7]
        self.quote = line[8]

class HashTable:
    #creates a table of size(capacitiy), keeps track of collisions and space used 
    def __init__(self,):
        self.collision = 0
        self.unusedSpace = 1
        self.table = [None]
        #creates list at each spot
    
    #adds a value into the hashtable
    #the key takes in the hashfunction output
    def add(self, key, name):
        #if the key is bigger than the size of the table
        if key > len(self.table)-1:
            value = ((key-len(self.table))+1)
            self.table.extend([None] * ((key-len(self.table))+1))
            self.unusedSpace += (value)
            self.table[key] = name
            self.unusedSpace -= 1
        #if there is already a value, at the spot it steps forward
        elif self.table[key] != None:
            self.collision += 1
            self.add(key + 19, name)
        #nothing there, then it sets the spot equal to your value
        else:
            self.table[key] = name
            self.unusedSpace -= 1

#Takes in a string and converts it to a integer
def hashFunction(stringData,listLength):
    #keeps track of the sum
    sum_of_chars = 0
    #loops through the string, getting the unicode value of each character
    for char in stringData:
        sum_of_chars += ord(char)
    squared = sum_of_chars ** 2
    string = str(squared)
    length = len(string)//3
    string = string[length:len(string)-length]
    #return the remainder of the string divided by the lenth of the table 
    return int(string) % (listLength)
print("Optimization technique: Mid-square hashing and linear probing by prime number collision technique")

#create both movie and quote hash Tables without set sizes
movie = HashTable()
quote = HashTable()

#read in data and inputs into movie table
file = "MOCK_DATA.csv"
counter = 0
start = time.time()
with open(file, 'r', newline = '', encoding = "utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if counter == 0:
            counter+=1
            continue
        newItem = DataItem(row)
        movie.add(hashFunction(newItem.movie_name,len(movie.table)),newItem)
        counter+=1
end = time.time()
print(f"The movie table had {movie.collision} collision")
print(f"The movie table has {movie.unusedSpace} unused spaces")
print(f"How much of the data was inputted {counter}")
print(f"The length of the table: {len(movie.table)}")
print(f"{end-start:0.2f} seconds")

       
#read in data and inputs into quote table
quote = HashTable()
file = "MOCK_DATA.csv"
counter = 0
start = time.time()
with open(file, 'r', newline = '', encoding = "utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if counter == 0:
            counter+=1
            continue
        newItem = DataItem(row)
        quote.add(hashFunction(newItem.quote,len(quote.table)),newItem)
        counter+=1  
end = time.time()
print(f"The quote table had {quote.collision} collision")
print(f"The quote table has {quote.unusedSpace} unused spaces")
print(f"How much of the data was inputted {counter}") 
print(f"The length of the table: {len(quote.table)}") 
print(f"{end-start:0.2f} seconds")