import libhearingdownloader
import os


#downloaders = {
#    "Phonak Target Downloader": "Phonak Target Downloader.py",
#    "Signia Connexx Downloader": "Signia Connexx Downloader.py",
#    "Rexton Connexx Downloader": "Rexton Connexx Downloader.py",
#    "Oticon Genie Downloader": "Oticon Genie Downloader.py",
#    "Oticon Genie 2 Downloader": "Oticon Genie 2 Downloader.py",
#    "Unitron TrueFit Downloader": "Unitron TrueFit Downloader.py",
#    "Widex Compass GPS Downloader": "Widex Compass GPS Downloader.py",
#    "Bernafon OasisNXT Downloader": "Bernafon OasisNXT Downloader.py",
#    "GN ReSound Downloaders": "GN ReSound Downloaders.py",
#    "GN Interton Downloaders": "GN Interton Downloaders.py",
#    "GN Beltone Downloaders": "GN Beltone Downloaders.py"
#}

downloaders = [
    ("Phonak Target Downloader", "", "Phonak Target Downloader.py"),
    ("Signia Connexx Downloader", "", "Signia Connexx Downloader.py"),
    ("Rexton Connexx Downloader", "", "Rexton Connexx Downloader.py"),
    ("Oticon Genie Downloader", "", "Oticon Genie Downloader.py"),
    ("Oticon Genie 2 Downloader", "", "Oticon Genie 2 Downloader.py"),
    ("Unitron TrueFit Downloader", "", "Unitron TrueFit Downloader.py"),
    ("Widex Compass GPS Downloader", "", "Widex Compass GPS Downloader.py"),
    ("Bernafon OasisNXT Downloader", "", "Bernafon OasisNXT Downloader.py"),
    ("GN ReSound Downloaders", "", "GN ReSound Downloaders.py"),
    ("GN Interton Downloaders", "", "GN Interton Downloaders.py"),
    ("GN Beltone Downloaders", "", "GN Beltone Downloaders.py")
]

disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by any of the companies mentioned in this repository",
    "Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]
libhearingdownloader.printDisclaimer(disclaimer)

print("==================================================")
print("=    Universal Hearing Aid Software Downloader   =")
print("========================================= " + libhearingdownloader.downloaderVersion + " =")
if (os.name != "nt"):
    print("NOTE: You are running this on a Unix (Or *NIX) Operating System, downloaded software is only available for Windows, but can still be downloaded via a Unix (Or *NIX) OS")
print("")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "downloader", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')