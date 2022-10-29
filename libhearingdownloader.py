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

def selectTargetVersion(validVersions):
    targetVersion = ''
    while not targetVersion:
        print("\n\n")
        versionIndex = 0
        for version in validVersions:
            if (version[1] != "--"):
                print(str(versionIndex) + ". " + version[0] + "\t" + version[1])
                versionIndex += 1
            else:
                print(version[0])
        
        try:
            targetVersion = int(input("Please select a version: "))
        except ValueError:
            targetVersion = -1
        
        if (targetVersion >= 0 and targetVersion < len(validVersions)):
            if (input("You have selected version (" + validVersions[targetVersion][0] + ") are you sure you want to download it? [Y/n] ") == "n"):
                targetVersion = ''
            else:
                return targetVersion
        else:
            print("The version you have selected is invalid.\nPlease try again.")
            targetVersion = ''

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