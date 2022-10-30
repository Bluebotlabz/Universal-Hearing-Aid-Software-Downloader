import requests
import math
import os

def normalizePath(path):
    if (path[-1] != "/"):
        path += "/"
    return path

def printDisclaimer(disclaimer):
    disclaimerWidth = 150
    print("\n\n")
    print ("="*disclaimerWidth)
    for line in disclaimer:

        paddedLine = line
        leftPad = (disclaimerWidth-len(paddedLine))/2
        rightPad = (disclaimerWidth-len(paddedLine))/2

        if (leftPad % 1 != 0):
            leftPad = math.floor(leftPad) + 1
            rightPad = math.floor(rightPad)
        
        leftPad = int(leftPad)
        rightPad = int(rightPad)

        print("=" + " "*(leftPad-1) + line + " "*(rightPad-1) + "=")
    print ("="*disclaimerWidth)
    input("Press enter to continue...")

def selecttargetIndex(validVersions):
    targetIndex = ''
    while not targetIndex:
        print("\n\n")
        indexMap = {} # Map version numbers to list index
        listIndex = 0 # The current index in the list
        selectionNumber = 0 # The current DISPLAYED index in the list

        for version in validVersions:
            if (version[1] != "--"):
                print(str(selectionNumber) + ". " + version[0] + "\t" + version[1])
                indexMap[selectionNumber] = listIndex
                selectionNumber += 1 # Increment displayed index
            else:
                print(version[0]) # Header
            listIndex += 1 # Increment list index
        
        try:
            targetIndex = int(input("Please select a version: "))
        except ValueError:
            targetIndex = -1
        
        if (targetIndex >= 0 and targetIndex <= selectionNumber):
            if (input("You have selected version (" + validVersions[indexMap[targetIndex]][0] + ") are you sure you want to download it? [Y/n] ") == "n"):
                targetIndex = ''
            else:
                return indexMap[targetIndex]
        else:
            print("The version you have selected is invalid.\nPlease try again.")
            targetIndex = ''

def selectOutputFolder():
    outputDir = ''
    while not outputDir:
        outputDir = normalizePath(input("Enter an output directory: "))
        if (input("Confirm download path (" + outputDir + ") [Y/n] ") == "n"):
            outputDir = ''
    
    return outputDir

def downloadFile(url, saveLocation):
    os.makedirs('/'.join(saveLocation.split("/")[:-1]), exist_ok=True) # Create path if it doesn't exist
    fileData = requests.get(url) # Get file
    if (fileData.status_code != 404):
        with open(saveLocation, 'wb') as file: # Write file content
            file.write(fileData.content)
    else:
        print("\n\nERROR: 404 File not found")
        exit()