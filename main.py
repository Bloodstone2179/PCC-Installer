from tkinter import *
from urllib.request import urlretrieve
from zipfile import ZipFile 
import tempfile, json, shutil, sys, argparse
global installLocation
arg = argparse.ArgumentParser("PCC INDSTALLER", "rawww")
arg.add_argument("--testing", type=bool, default=False, required=False)
args = arg.parse_args()
installLocation = input("Enter The Location Where You Want To Install PCC to: ")#
def DownloadGCC():
    url = ("https://github.com/brechtsanders/winlibs_mingw/releases/download/13.2.0posix-17.0.6-11.0.1-ucrt-r5/winlibs-x86_64-posix-seh-gcc-13.2.0-mingw-w64ucrt-11.0.1-r5.zip")
    filename = tempfile.gettempdir() + "/gcc.zip"
    a, headers = urlretrieve(url, filename)
    print(headers["Content-Length"])
    print(f"Downloading G++, Size: {round(((int(headers["Content-Length"]) / 1024) / 1024), 2)} MB")
    
    urlretrieve(url, filename)
    print("Downloading Finished")

def UnzipGCC():
    print(f"Extracting G++ To {installLocation}/g++_install/")
    path = tempfile.gettempdir() + "/gcc.zip"
    extractLocation = installLocation + "/g++_install/"
    with ZipFile(path, 'r') as zObject:
        zObject.extractall(path=extractLocation)
    print("Extraction Finished")

def DownloadPCC():
    print("Downloading PCC")
    url_vf = ("https://raw.githubusercontent.com/Bloodstone2179/PCC/master/VersionFile.json")
    urlretrieve(url_vf, "vers.json")
    y = json.loads(open("vers.json").read())
    print(y["LatestReleaseVersion"])
    url_h = (f"https://github.com/Bloodstone2179/PCC/releases/download/{y["LatestReleaseVersion"]}/builtins.h")
    url_pcc = (f"https://github.com/Bloodstone2179/PCC/releases/download/{y["LatestReleaseVersion"]}/pcc.exe")
    filename_pcc = installLocation + "/pcc.exe"
    filename_h = installLocation + "/builtins.h"
    urlretrieve(url_pcc, filename_pcc)
    urlretrieve(url_h, filename_h)
    print("PCC Finshed Downloading\nEverything Is Now Installed Have A Good day <3")

if args.testing == False:
    DownloadGCC()
    UnzipGCC()
    DownloadPCC()
if args.testing == True:
    #copy over the builtins file and the built exe to replace the 1 in install location
    y = json.loads(open("AQA PseudoCode transpiler/VersionFile.json").read())
    print(y["LatestReleaseVersion"])
    currentversion = y["LatestReleaseVersion"]
    pccDevLocation = "AQA PseudoCode transpiler/Releases/Win64/" + currentversion
    shutil.copyfile(pccDevLocation + "/pcc.exe", installLocation + "/pcc.exe")
    shutil.copyfile("AQA PseudoCode transpiler/SRC/builtins.h", installLocation + "/builtins.h")
    print(pccDevLocation)
    pass