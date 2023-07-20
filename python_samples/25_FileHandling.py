# reading file 


def customReadFileusingRead(filename):
    try:
        file = open(filename)
        # similar code below
        # file = open("demofile3.txt", "rt")
        print ("Read file contents using read method")
        contents = file.read()
        return contents
    
    except:
        raise Exception("Exception raised while reading the file...")
    finally:
        file.close()



def customReadFileUsingReadLines(fileName):
    try:
        file = open(fileName)
        # similar code below
        # file = open("demofile3.txt", "rt")

        print ("Read file contents using read method")
        contentsInLines = file.readlines()
        return contentsInLines
    except:
        raise Exception("Exception raised while reading the file")
    finally:
        file.close()


content = customReadFileusingRead("sampletext.txt")
print (f"using read: {content}")
content = customReadFileUsingReadLines("samplefile.txt")
print (f"using readLines: {content}")


# read only part of the file using read command 
file = open("samppletext.txt")
print ("Read only 10 characters from a file using read method : ")
print (file.read(10))
file.close()

# read only part of file using read commnand 
file = open("sampletext.txt")
print ("Read only 10 characters from a file using read method : ")
print (file.readline())


### write / create file using mode w 

def customFileWriter(fileName, mode, content):
    file = open(fileName, mode)
    file.write(content)
    file.close()


customFileWriter("demofile3.txt", "w", "This is my first line.\n")
customFileWriter("demofile3.txt", "w", "This is my second line.\n")
customFileWriter("demofile3.txt", "w", "This is my third line.\n")


def printFileContents(filename):
    file = open(filename)
    print (file.readlines())
    file.close()

printFileContents("demofile3.txt")


# delete file
import os
# os.remove("demofile4.txt")


# check if file exists 
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print ("The file does not exist")

# delete folder
# os.rmdir("myfolder")