import os

## how about using name from relational algebra
def rename(csvFile, headers):
    if type(headers) is str:
        renameFromList(headers)
    elif type(headers) is dict:
        renmaeFromDict(headers)
    else:
        print("please input valid headers")

def renameFromString(csvFile, headerString):
    targetFile = csvFile + ".tmp"
    renameSedCommand = "sed '1 s/^.*$/{0}/' {1} > {2}".format(headerString, csvFile, targetFile)
    stream = os.popen(renameSedCommand)
    print(stream.read())

    return targetFile

def renmaeFromDict(csvFile, headDict, sep = ','):
    ## todo we need to support partial rename by using dict
    pass 

def filter():
    pass 


## todo only support delete the fied by name right now 
def filterCols(csvFile, colsDeletedList, sep = ','):    
    targetCsvFile = csvFile + ".tmp"
    fieldNameIdx = getFieldNameIdx(csvFile, sep)

    filteredFiledIdx = [v for k, v in fieldNameIdx.items() if k not in colsDeletedList]
    sepString = "\"" + sep + "\""
    printString = sepString.join(["$" + str(idx) for idx in fieldNameIdx])
    awkPrintCommand = " ".join(["awk -F", sep, printString, csvFile])
    awkPrintCommand = "awk -F '{0}' '{{print {1}}} {2} > {3}'".format(sep, printString, \
        csvFile, targetCsvFile)

    print("start to execute awk command:{0}".format(awkPrintCommand))
    stream = os.popen(awkPrintCommand)
    print(stream.read())

    return targetCsvFile


def getFieldNameIdx(csvFile, sep=','):
    with open(csvFile) as f:
        headers = f.readline()
        fileds = headers.split(sep)
        return {name: i + 1 for i, name in enumerate(fileds)}


def filterRows(csvFile, boolExpr, sep = ','):
    targetFile = csvFile + ".tmp"

    awkCommand = "awk -F '{0}' '{{if({1}) {{print}}}}\' {2} > {3}".format(sep, \
        boolExpr, csvFile, targetFile)
    
    print("filterRows, begin to execute awk command: {0}".format(awkCommand))
    stream = os.popen(awkCommand)
    print(stream.read())

    return targetFile

def transform(csvFile, transformExpre, sep = ","):
    targetFile = csvFile + ".tmp"
    awkCommand = "awk -F '{0}' '{{ {1} print}}' {2} > {3}".format(sep, transformExpre, csvFile, \
        targetFile)

    print("transform, begin executing awk command:{0}".format(awkCommand))
    stream = os.popen(awkCommand)

    print(stream.read())
    return targetFile 

def diff(csv1, csv2, sep=','):
    tragetFile = csv1 + csv2
    ## todo get to familiar with 
    diffCmd  = "diff {0} {1} > {2} ".format(csv1, csv2, tragetFile)

    print("diff, start to execute diff")
    stream = os.popen(diffCmd)
    print(stream.read())

    return tragetFile

def merge(csv1, csv2):
    targrtFile =  csv1 + csv2 + ".tmp"
    mergeCmd = "cat {0} {1} > {2}" 
    print("merge ,start to execute command:{0}".format(mergeCmd))

    stream = os.popen(mergeCmd)

    print(stream.read())

    return targrtFile

