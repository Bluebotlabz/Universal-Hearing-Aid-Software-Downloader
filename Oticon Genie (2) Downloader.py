#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import libhearingdownloader
import xml.etree.ElementTree as xml
utilityVersion = "v1.1.2"
verboseDebug = False



print("==================================================")
print("=           Oticon Genie (2) Downloader          =")
print("="*(47-len(utilityVersion)) + " " + utilityVersion + " =")

disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "Oticon is a trademark of Oticon",
    "Sonova is a trademark of Sonova AG",
    "Oticon is a subsidiary of Sonova AG",
    "Oticon Genie & Oticon Genie 2 are created by Oticon",
    "All rights and credit go to their rightful owners. No copyright infringement intended."
    "",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by Oticon or Sonova AG",
    "Depending on how this software is used, it may breach the EULA of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]

# Display disclaimer
libhearingdownloader.printDisclaimer(disclaimer)


# Define list of valid versions and their download links (direct from CDN)
validVersions = [
    ("Online Installers (shorter downloads, but they require an internet connection to install)", "--"),
    ("Genie 2 2022.1.0", "The latest Genie 2 2022.1.0 Installer", "https://installcdn.oticon.com/22.1/15.19.13.0/Genie/Oticon/47b1876d/setup.exe"),
    ("Genie 2 2020.1", "The Genie 2 2020.1 Installer", "https://installcdn.oticon.com/20.1/9.3.116.0/Genie/Oticon/9fc0827f/setup.exe"),
    ("Genie 2017.1", "The last Genie 1 2017 Version", "https://installcdn.oticon.com/full/17.1/27.0.40.29/OTG214672OT_USB.zip"),
    ("Genie Medical 2016.1", "The old Genie 1 2016 Version", "https://wdh02.azureedge.net/-/media/oticon-us/main/client-systems-support-and-remote-assistance/geniemedical2016.exe?la=en&rev=171A&hash=95AF6010585FD97B23A9FAB05FBAE761"),
    ("", "--"),
    ("Offline Installers (longer downloads, but they work without an internet connection to install)", "--"),
    ("Genie 2 2022.1.0", "The latest Genie 2 2022.1.0 Installer (OFFLINE INSTALLER)", "https://installcdn.oticon.com/full/22.1/15.19.13.0/OTG22_1237118OT_USB.zip"),
    ("Genie 2 2020.1", "The Genie 2 2020.1 Installer (OFFLINE INSTALLER)", "https://installcdn.oticon.com/full/20.1/9.3.116.0/OTG20_1214671OT_USB.zip")
]

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = libhearingdownloader.selectTargetVersion(validVersions)
print("\n\n")

# Create download folder
outputDir += '.'.join(validVersions[targetVersion][0].split('.')[:-1]) + "/"

if(verboseDebug):
    print("V:" + str(targetVersion))
    print("T:" + validVersions[targetVersion])

# Print download messages
print("Downloading " + validVersions[targetVersion][0])
print("This may take a while...")

# Download the file
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + validVersions[targetVersion][2].split("/")[-1])

print("\n\nDownload Complete!")
