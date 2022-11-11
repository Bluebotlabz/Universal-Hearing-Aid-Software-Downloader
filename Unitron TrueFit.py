#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import requests
import libhearingdownloader
import xml.etree.ElementTree as xml
utilityVersion = "v1.6.2"
verboseDebug = False



print("==================================================")
print("=           Unitron TrueFit Downloader           =")
print("="*(47-len(utilityVersion)) + " " + utilityVersion + " =")

disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "Unitron is a trademark of Sonova AG",
    "Sonova is a trademark of Sonova AG",
    "Unitron is a subsidiary of Sonova AG",
    "Unitron TrueFit is created by Unitron",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by Unitron or Sonova AG",
    "Depending on how this software is used, it may breach the EULA of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]

# Display disclaimer
libhearingdownloader.printDisclaimer(disclaimer)
print("\n\n")



print("Fetching Data...")
# Yh that's right, Phonak namespace...
xmlns = "{http://cocoon.phonak.com}" # Define the xmlns
xmlData = requests.get("https://svc.myunitron.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=Unitron%20TrueFit&appVer=5.1.0.25391&dist=Unitron&country=GB&subKeys=").text # Request the updater API (spoof older version to get whole installer files rather than "patch" installers)
data = xml.fromstring(xmlData)

# Get latest version number (Gets full version from xml and removes the fourth version number as that is not used in files)
latestVersion = '.'.join((data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text).split(".")[:-1])


# List of versions
validVersions = [
    (latestVersion, 'The latest available Unitron TrueFit verion'),
    ('manual', 'Manually specify a version (WARNING: ADVANCED USERS ONLY)')
]

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = validVersions[libhearingdownloader.selectTargetVersion(validVersions)][0]
print("\n\n")


# Logic for "special" versions
if (targetVersion == 'latest'):
    targetVersion = latestVersion
elif (targetVersion == 'manual'):
    targetVersion = ''
    while not targetVersion:
        targetVersion = input("Please enter manual target version: ")
        if (len(targetVersion.split('.')) > 3 or not targetVersion.replace('.', '').isdecimal()):
            print("The version you have selected is invalid.\nPlease try again. (hint: it should be in a similar format to a.b.c where a, b, and c are integers)")
        elif (input("You have selected version (" + targetVersion + ") are you sure you want to download it? [Y/n] ") == "n"):
            targetVersion = ''

# Create download folder
outputDir += "Unitron TrueFit " + targetVersion + "/"

# Get CDN/Download location
unitronCDNPath = data[0].find(xmlns + "Location").text

# Get list of files to download for a specified version from the XML data
print ("Downloading directory index")
filesToDownload = {}
for child in data[0].find(xmlns + "ContentInfos"):
    # Construct paths
    filesToDownload[(outputDir + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)] = (libhearingdownloader.normalizePath(unitronCDNPath, False) + libhearingdownloader.normalizePath(child.find(xmlns + "RemotePath").text, False) + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)

# Download and save the files
print("Downloading " + str(len(filesToDownload.keys())) + " files\n")
currentFile = 1
for fileToDownload in filesToDownload.keys():
    if (verboseDebug):
        print(filesToDownload[fileToDownload])

    # Download file
    libhearingdownloader.downloadFile(filesToDownload[fileToDownload], fileToDownload, "Downloading " + fileToDownload.split("/")[-1] + " (" + str(currentFile) + "/" + str(len(filesToDownload.keys())) + ")")

    currentFile += 1

print("\n\nDownload Complete!")
