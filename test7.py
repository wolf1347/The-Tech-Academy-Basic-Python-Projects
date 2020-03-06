
import os


def writeData():
    data = '\nAnd this is being added via an append. \nOtherwise if you use W it would overwrite'
    with open('test.txt','a') as f:
        f.write(data)
        f.close()
        
def openFile():
    with open('test.txt','r') as f:
        data = f.read()
        print(data)
        f.close()


if __name__ == "__main__":
    writeData()
    openFile()

