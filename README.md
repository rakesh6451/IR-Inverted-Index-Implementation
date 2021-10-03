# IR-Inverted-Index-Implementation
This is the implementation of inverted index in python
Problem statement:Creating inverted index for the given dataset.
Language:Python3

Packages to install(Process for executing the file):
-->Install nltk using the command "pip install nltk".
-->After installing, in nltk.stem, import PorterStemmer.
-->Other libraries required are already present with python.
-->Now run the python file with the command "python3 filename.py" in terminal.
-->This file takes the dataset as a input and output will generated in the output file

Datastructures used:
Arrays(lists in python3) and Hashtables(dictionary in python3)

Time Complexity analysis:
     O(m*n*r) where  
          m =>Total number of documents 
          n => Total number of words in each document
          r => Average word-size 
          m*n*r =>Total number of characters in all the documents
		We can neglect r.
		Hence, Time complexity is O(m*n).  

Space Complexity analysis:
     m =>Total number of documents 
     n =>Total number of unique words 
        Hence, Space complexity is O(m*n)


Details about the implementation part:
class Listofpostings: This class will take document id and its frequency and create a seperate  posting list.

class BuildInvertedindex:It will intialise an empty dictionary.The methods in this class will process
 the sequence of characters and tokenize them to appropriate terms for the dictionary.
    
def wordtokenize(self, templist):This method will process the terms by removing stopwards , it will use
 “Porter’s Stemmer” to stem the rootword.

def docretrieval(self, documentindex, documentmatter):This method takes words from each document and adds the frequency of each word.

def dictterms(self, dir_path):This method takes each file from the dataset folder and in turn  sends this
 document to docretrieval method for the further processings.

def extractindex(self, resultdocument="Assign012019052-output"):This method prints the output of each 
term in posting list to a new output file named "Assign012019052-output" with frequency  of total number of 
text files.





