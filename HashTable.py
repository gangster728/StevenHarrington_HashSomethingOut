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

    #Add/list appending collision
        #attempts to add at the index it recieved from the hash function
        #if there is nothing there, then it inputs it at this spot
        #if there is something there, then it appends to the end of the list attatched at the spot



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
    def __init__(self,capacity):
        self.collision = 0
        self.unusedSpace = capacity
        self.capacity = capacity
        self.table = [None] * capacity
        #creates list at each spot
        for i in range(capacity):
            self.table[i] = [None]
    
    #adds a value into the hashtable
    #the key takes in the hashfunction output
    def add(self, key, name):
        #if there is already a value, it adds to the end of the list at that index
        if self.table[key][0] != None:
            
            self.collision += 1
            self.table[key].append(name)
           
        #nothing there, then it sets the spot equal to your value
        else:
            self.table[key][0] = name
            self.unusedSpace -= 1

#Takes in a string and converts it to a integer
def hashFunction(stringData):
    #keeps track of the sum
    sum_of_chars = 0
    #loops through the string, getting the unicode value of each character
    for char in stringData:
        sum_of_chars += ord(char)
    squared = sum_of_chars ** 2
    string = str(squared)
    length = len(string)//3
    string = string[length:len(string)-length]
    return int(string) % 997
print("Optimization technique: Mid-square hashing and list appending collision technique")

#create both movie and quote hash Tables
movie = HashTable(997)
quote = HashTable(997)

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
        movie.add(hashFunction(newItem.movie_name),newItem)
        counter+=1
end = time.time()
print(f"The movie table had {movie.collision} collision")
print(f"The movie table has {movie.unusedSpace} unused spaces")
print(f"How much of the data was inputted {counter}")
print(f"{end-start:0.2f} seconds")


       
#read in data and inputs into quote table
quote = HashTable(997)
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
        quote.add(hashFunction(newItem.quote),newItem)
        counter+=1  
end = time.time()
print(f"The quote table had {quote.collision} collision")
print(f"The quote table has {quote.unusedSpace} unused spaces")
print(f"How much of the data was inputted {counter}")  
print(f"{end-start:0.2f} seconds")