import os

## todo how to implement a linux pipeline?
## todo organize it by the class , and then do the final test, and then consider the high level interface.
## todo consider to give a front end??? to make it a very general platform, consider the Jenkins design
## todo consider more to be a very general platform
## todo here 
## todo here 

## todo here 
## todo here 
## todo here 
## todo here 
## todo here 
## todo here 
## todo here 
## todo here 
## todo here 
## todo here 
## todo here 
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
def rename(csvFile, headerString):
    targetFile = csvFile + ".tmp"
    renameSedCommand = "sed '1 s/^.*$/{0}/' {1} > {2}".format(headerString, csvFile, targetFile)
    stream = os.popen(renameSedCommand)
    print(stream.read())

    return targetFile

def copyHeader(orign, to):
    line = ""
    with open(orign) as f:
        line  = f.readline()

    with open(to, 'w') as f:
        f.write(line)

def selection(csvFile, selectString, sep = ','):    
    print ("sep is :{0}".format(sep))
    targetCsvFile = csvFile + ".tmp"

    with open(targetCsvFile, 'w') as f:
        f.write(selectString)

    copyHeader(csvFile, targetCsvFile)
    fieldNameIdx = getFieldNameIdx(csvFile, sep)

    filteredFiledIdx = [v for k, v in fieldNameIdx.items() if k in selectString]
    sepString = "\"" + sep + "\""

    printString = sepString.join(["$" + str(idx) for idx in filteredFiledIdx])

    awkPrintCommand = "awk -F '{0}' '{{print {1}}}' {2} >> {3}".format(sep, printString, \
        csvFile, targetCsvFile)

    print("start to execute awk command:{0}".format(awkPrintCommand))
    stream = os.popen(awkPrintCommand)
    print(stream.read())

    return targetCsvFile


def getFieldNameIdx(csvFile, sep=','):
    with open(csvFile) as f:
        headers = f.readline()
        fileds = headers.split(sep)
        return {name.strip(): i + 1 for i, name in enumerate(fileds)}


def where(csvFile, boolExpr, sep = ','):
    targetFile = csvFile + ".tmp"
    copyHeader(csvFile, targetFile)
    awkCommand = "awk -F '{0}' '{{if({1}) {{print}}}}\' {2} >> {3}".format(sep, \
        boolExpr, csvFile, targetFile)
    
    print("filterRows, begin to execute awk command: {0}".format(awkCommand))
    stream = os.popen(awkCommand)
    print(stream.read())

    return targetFile

def transform(csvFile, transformExpre, sep = ","):
    targetFile = csvFile + ".tmp"
    copyHeader(csvFile, targetFile)
    awkCommand = "awk -F '{0}' '{{ {1} print}}' {2} >> {3}".format(sep, transformExpre, csvFile, \
        targetFile)

    print("transform, begin executing awk command:{0}".format(awkCommand))
    stream = os.popen(awkCommand)

    print(stream.read())
    return targetFile 

## todo how to define the format ? how ? do we need this interface ?
def diff(csv1, csv2, sep=','):
    leftFile = diffLeft(csv1, csv2, sep)
    rightFile = diffRight(csv1, csv2 , sep)
    commFile = diffComm(csv1, csv2, sep)

    diffFile = csv1 + csv2 + ".diff"

    return  ""



def diffLeft(csv1, csv2, sep=','):
    leftFile = csv1 + ".leftdiff"
    ## todo get to familiar with
    diffLeft = "comm  -23 {0} {1} > {2} ".format(csv1, csv2, leftFile)


    print("diff, start to execute diff")
    stream = os.popen(diffLeft)
    print(stream.read())

    return leftFile


def diffRight(csv1, csv2, sep=','):
    rightFile = csv2 + ".rightdiff"

    diffRight = "comm  -13 {0} {1} > {2} ".format(csv1, csv2, rightFile)

    print("diff, start to execute diff")
    stream = os.popen(diffRight)
    print(stream.read())

    return rightFile


def diffComm(csv1, csv2, sep=','):
    commonfile = csv1 + csv2 + ".comm"

    diffComm = "comm  -12 {0} {1} > {2} ".format(csv1, csv2, commonfile)
    print("diff, start to execute diff")
    stream = os.popen(diffComm)
    print(stream.read())

    return commonfile


def merge(csv1, csv2):
    targrtFile =  csv1 + csv2 + ".tmp"
    
    csv2_tmp = csv2 + ".tmp"
    deleteFirstLineCommand = "sed '1d' {0} > {1}".format(csv2, csv2_tmp)
    stream = os.popen(deleteFirstLineCommand)
    print(stream.read())

    mergeCmd = "cat {0} {1} > {2}".format(csv1, csv2_tmp, targrtFile)
    print("merge ,start to execute command:{0}".format(mergeCmd))

    stream = os.popen(mergeCmd)

    print(stream.read())
    os.remove(csv2_tmp)

    return targrtFile

## todo replace the delimiter, how
def delimiter(origin, to):
    pass
