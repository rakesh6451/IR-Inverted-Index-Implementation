#importing libraries
from os import listdir
from os.path import isfile, join
from nltk.stem import PorterStemmer
import json
from os import getcwd, path

#class representing the posting list
class Listofpostings:
    def __init__(self, filename, occurences) -> None:
        self.filename = filename.split(".")[0]
        self.occurences = occurences

    def __str__(self) -> str:
        return f"({self.filename},{self.occurences})"

#class for inverted index
class BuildInvertedindex:
    
    def __init__(self) -> None:
        self.posting = dict()

    
    def wordtokenize(self, templist):

        if "“" in templist:
            templist = templist.replace("“", "")

        if "”" in templist:
            templist = templist.replace("”", "")
        
        if "’" in templist:
            templist = templist.replace("’", "")

        if "‘" in templist:
            templist = templist.replace("‘", "")
 
        if "&" in templist:
            templist = templist.replace("&", "")        

        if "\n" in templist:
            templist = templist.replace("\n", "")

        if "," in templist:
            templist = templist.split(",")[0]
        
        if "." in templist:
            templist = templist.replace(".", "")

        if "'" in templist:
            templist = templist.replace("'", "")
        if "(" in templist:
            templist=templist.replace("(","")
        if ")" in templist:
            templist=templist.replace(")","")
        if "-" in templist:
            templist=templist.replace("-","")
        
    
        stemmer = PorterStemmer()
        return stemmer.stem(templist)
    

    def docretrieval(self, documentindex, documentmatter):
        print(f"Processing file {documentindex}...")
        file_terms = dict()
        words = documentmatter.split(" ")

        for word in words:
            word = self.wordtokenize(word)

            if word in file_terms.keys():
                file_terms[word] += 1
            else:
                file_terms[word] = 1
        
        for posi in file_terms.items():
            term, occurences = posi
            posting_list_item = Listofpostings(documentindex, occurences)
            if term in self.posting.keys():
                self.posting[term].append(posting_list_item)
            else:
                self.posting[term] = list([posting_list_item])


    def dictterms(self, dir_path):
        tempdocs = [ tem1 for tem1 in listdir(dir_path) if isfile(join(dir_path, tem1))]
        print(f"directory is processing {dir_path}")
        print(f"{len(tempdocs)} found")
        for tem1 in tempdocs:
            documentmatter = open(join(dir_path, tem1), encoding='utf-8')
            self.docretrieval(tem1, documentmatter.read())
    
    def extractindex(self, resultdocument="Assign012019052-output"):
        print(f"printing results to {resultdocument}.txt....")
        for posi in list(self.posting.items()):
            firstl, secondl  = posi
            resultstr = f"{firstl} : "
            posting_list = "".join([f"{str(posting_item.filename)}," for posting_item in secondl])
            resultstr += f"( {len(secondl)} , [{posting_list}])\n" 
            with open(f"{resultdocument}.txt", 'a', encoding="utf-8") as tem1:
                tem1.write(resultstr)

#main function            
if __name__ == "__main__":
    
    #loading the dataset
    Pathpos= path.abspath(getcwd()) + r"\th-dataset"
    #creating the objects
    obj_invertedindex = BuildInvertedindex()
    obj_invertedindex.dictterms(dir_path=Pathpos)

    obj_invertedindex.extractindex()
   
