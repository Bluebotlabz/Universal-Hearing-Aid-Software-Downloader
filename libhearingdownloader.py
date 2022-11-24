from tqdm import tqdm
import requests

try:
    import wx
    guiType = "wxpython"
except:
    try:
        from tkinter import filedialog as tkfiledialog
        from tkinter import Tk
        guiType = "tkinter"
    except:
        guiType = None

import time
import math
import os


###
# libhearingdownloader - A useful library for the downloader scripts
###

downloaderVersion = "v1.7.4"
updaterRetries = 3
verboseDebug = False

def normalizePath(path, correctWindowsChars=True):
    if (path[-1] != "/"):
        path += "/"

    if (correctWindowsChars):
        return (path.replace("|", "-").replace("<", "-").replace(">", "-").replace(":", "-").replace('"', "-").replace("?", "-").replace("*", "-"))
    else:
        return path

def printDisclaimer(disclaimer):
    disclaimerWidth = 150
    print("\n\n")
    print ("="*disclaimerWidth)
    for line in disclaimer:
        leftPad = (disclaimerWidth-len(line))/2
        rightPad = (disclaimerWidth-len(line))/2

        if (leftPad % 1 != 0):
            leftPad = math.floor(leftPad) + 1
            rightPad = math.floor(rightPad)
        
        leftPad = int(leftPad)
        rightPad = int(rightPad)

        print("=" + " "*(leftPad-1) + line + " "*(rightPad-1) + "=")
    print ("="*disclaimerWidth)
    input("Press enter to continue...")

def selectTargetVersion(validVersions, prompt = "version", headerSeperator='', seperator='\t'):
    targetIndex = ''
    while not targetIndex:
        print("\n\n")
        indexMap = {} # Map version numbers to list index
        listIndex = 0 # The current index in the list
        selectionNumber = 0 # The current DISPLAYED index in the list

        for version in validVersions:
            if (version[1] != "--"):
                print(str(selectionNumber) + ". " + version[0] + seperator + version[1])
                indexMap[selectionNumber] = listIndex
                selectionNumber += 1 # Increment displayed index
            else:
                print(headerSeperator + version[0]) # Header
            listIndex += 1 # Increment list index
        
        try:
            targetIndex = int(input("Please select a " + prompt + ": "))
        except ValueError:
            targetIndex = -1
        
        if (targetIndex >= 0 and targetIndex <= selectionNumber):
            if (input("You have selected " + prompt + " (" + validVersions[indexMap[targetIndex]][0] + ") are you sure you want to download it? [Y/n] ") == "n"):
                targetIndex = ''
            else:
                return indexMap[targetIndex]
        else:
            print("The " + prompt + " you have selected is invalid.\nPlease try again.")
            targetIndex = ''

def selectOutputFolder():
    if (guiType == "wxpython"):
        print("Please select a download location")
        time.sleep(2)

        wxApp = wx.App(redirect=False, useBestVisual=True, clearSigInt=True)
        wxDirDialog = wx.DirDialog(None, "Choose a download folder", "")
        dialogReturn = wxDirDialog.ShowModal()

        if (dialogReturn == wx.ID_CANCEL):
            print("No valid directory selected, exiting")
            exit()
        else:
            outputDir = wxDirDialog.GetPath()

        wxApp.Destroy()
    elif (guiType == "tkinter"):
        print("Please select a download location")
        time.sleep(2)

        tkRoot = Tk()
        tkRoot.withdraw()
        tkRoot.focus()
        tkRoot.focus_force()
        tkRoot.wm_attributes('-topmost', True)

        outputDir = tkfiledialog.askdirectory( parent=tkRoot, title="Choose a download folder")
        if (not outputDir):
            print("No valid directory selected, exiting")
            exit()

        tkRoot.destroy()
    elif (guiType == None):
        outputDir = ''
        while not outputDir:
            print("\n\n")
            outputDir = input("Enter an output directory: ")
            if (outputDir != ""):
                if (input("Confirm download path (" + normalizePath(outputDir, False) + ") [Y/n] ") == "n"):
                    outputDir = ''
            else:
                print("The directory you have selected is invalid.\nPlease try again.")
                outputDir = ''
    
    return normalizePath(outputDir, False)

def downloadFile(url, saveLocation, downloadDescription):
    os.makedirs('/'.join(saveLocation.split("/")[:-1]), exist_ok=True) # Create path if it doesn't exist
    fileData = requests.get(url, stream=True) # Get file stream

    chunkSize = 2048
    
    if (str(fileData.status_code)[0] != '2'):
        print("Error downloading file: [" + str(fileData.status_code) + "]")
        exit(1)

    fileSize = int(fileData.headers['content-length'])
    if (fileSize < chunkSize and fileSize > 0):
        chunkSize = fileSize

    if (fileData.status_code == 200):
        with open(saveLocation, 'wb') as fd:
            for chunk in tqdm(fileData.iter_content(chunk_size=chunkSize), desc=downloadDescription, total=int(int(fileData.headers['content-length'])/chunkSize), unit="B", unit_scale=chunkSize):
                fd.write(chunk)
    else:
        print("\n\nERROR: " + str(fileData.status_code))
        exit(1)