import os

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
    
    csv2_tmp = csv2 + ".tmp"
    deleteFirstLineCommand = "sed '1d' {0} > {1}".format

    mergeCmd = "cat {0} {1} > {2}".format(csv1, csv2, targrtFile)
    print("merge ,start to execute command:{0}".format(mergeCmd))

    stream = os.popen(mergeCmd)

    print(stream.read())

    return targrtFile

## todo replace the delimiter, how
def delimiter(origin, to):
    pass
