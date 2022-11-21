#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import requests
import libhearingdownloader
import xml.etree.ElementTree as xml

    

print("==================================================")
print("=           ReSound Software Downloader          =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + libhearingdownloader.downloaderVersion + " =")

disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "ReSound is a trademark of GN Hearing A/S and/or its affiliates (\"GN Group\")",
    "GN is a trademark of GN Store Nord A/S",
    "GN Hearing A/S is a subsidiary of GN Store Nord A/S",
    "ReSound is a subsidiary of GN Hearing A/S",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by ReSound, GN Hearing A/S, GN Group or GN Store Nord A/S",
    "Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]

# Display disclaimer
libhearingdownloader.printDisclaimer(disclaimer)

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Download update file list from updater API
        rawXmlData = requests.get("http://www.supportgn.com/resound/subsites/releasessdb.xml")
        data = xml.fromstring(rawXmlData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("Error: Update server could not be reached")
    exit(1)

if (libhearingdownloader.verboseDebug):
    print(rawXmlData.text)

# Define XMLNS (the main one)
availableFiles = [] # List of available files

for child in data:
    if (child[0].tag == "SEPARATOR"):
        availableFiles.append( ("== " + child[0].text + " ==", '--') )
    else:
        availableFiles.append( (child.find("BUTTONTEXTDOWN").text, child.find("LINK").text) )

if (libhearingdownloader.verboseDebug):
    print(availableFiles)

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()
targetFile = availableFiles[libhearingdownloader.selectTargetVersion(availableFiles, prompt="software", headerSeperator = '\n')]

if (libhearingdownloader.verboseDebug):
    print(targetFile)

targetURL = targetFile[1]

if (not ("http://" in targetURL or "https://" in targetURL)):
    targetURL = "http://www.supportgn.com/files/" + targetURL

# Create download folder
#outputDir += '.'.join(targetFile[0].split('.')[:-1]) + "/"
outputLocation = outputDir + '.'.join(targetFile[1].split("/")[-1].split(".")[:-1]) + "/" + targetFile[1].split("/")[-1]
print("\n\n")

# Download file
libhearingdownloader.downloadFile(targetURL, outputLocation, "Downloading " + targetFile[0])

print("\n\nDownload Complete!")