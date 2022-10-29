#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import requests
import libhearingdownloader
import xml.etree.ElementTree as xml
utilityVersion = "v1.1.0"
verboseDebug = False

    

print("==================================================")
print("=           Signia Connexx Downloader            =")
print("="*(47-len(utilityVersion)) + " " + utilityVersion + " =")

disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "Signia is a trademark of Signia GmbH",
    "Siavantos is a trademark of SIVANTOS PTE. LTD.",
    "Signia and Siavantos are subsidiaries of WS Audiology A/S",
    "WS Audiology A/S is a trademark of Widex A/S",
    "Widex is a trademark of Widex A/S",
    "Signia Connexx is created by Signia GmbH",
    "All rights and credit go to their rightful owners. No copyright infringement intended."
    "",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by Signia GmbH, SIVANTOS PTE. LTD., WS Audiology A/S or Widex A/S",
    "Depending on how this software is used, it may breach the EULA of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]

libhearingdownloader.printDisclaimer(disclaimer)
print("\n\n")



headers = {
    "Content-Type": "application/soap+xml; charset=utf-8",
    "Connection": "Keep-Alive"
}

# Download directly from Signia to avoid copyright
rawXmlData = requests.post("https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackages</a:Action><a:MessageID>urn:uuid:c6a24c9d-0a1a-4fd2-b6c2-f4da34663374</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc</a:To></s:Header><s:Body><GetPackages xmlns="http://tempuri.org/"><products xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ProductInfo><b:CurrentVersion>19.7.0.144</b:CurrentVersion><b:ProductName>Update Manager</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>4767b7e4-7f3c-4a64-8cb5-e80b23b1458b</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>9.7.0.144</b:CurrentVersion><b:ProductName>Programmer</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>4767b7e4-7f3c-4a64-8cb5-e80b23b1458b</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>9.7.0.548</b:CurrentVersion><b:ProductName>SigniaConnexx</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>4767b7e4-7f3c-4a64-8cb5-e80b23b1458b</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>9.7.0.144</b:CurrentVersion><b:ProductName>Support Tools</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>4767b7e4-7f3c-4a64-8cb5-e80b23b1458b</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>4.8.0.0</b:CurrentVersion><b:ProductName>DotNetFramework</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>6.0.5.00</b:CurrentVersion><b:ProductName>DotNetCoreRuntime</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>10.0.22.0</b:CurrentVersion><b:ProductName>OperatingSystem</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>14.32.31.00</b:CurrentVersion><b:ProductName>VC2015Redistributable</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>GB</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo></products></GetPackages></s:Body></s:Envelope>')
data = xml.fromstring(rawXmlData.text)

if (verboseDebug):
    print(rawXmlData.text)

packageXMLNS = '{http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS}'
availableFiles = []

for child in data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "PackageFiles"):
    availableFiles.append( (child.find(packageXMLNS + "FileName").text, child.find(packageXMLNS + "DownloadURL").text) )

if (verboseDebug):
    print(availableFiles)

outputDir = libhearingdownloader.selectOutputFolder()
targetFile = list(availableFiles)[libhearingdownloader.selectTargetVersion(availableFiles)]

print("\n\n")

print("Downloading file [" + targetFile[0] + "]")
print("This may take a while...")

libhearingdownloader.downloadFile(targetFile[1], outputDir + targetFile[0])

print("\n\nDownload Complete!")