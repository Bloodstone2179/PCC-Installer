from urllib.request import urlretrieve
from zipfile import ZipFile 
import tempfile, json, shutil, argparse
from os import getcwd
import os
global installLocation
arg = argparse.ArgumentParser("PCC INSTALLER")
arg.add_argument("--testing", type=bool, default=False, required=False,action=argparse.BooleanOptionalAction)
arg.add_argument("--update", type=bool, default=False, required=False,action=argparse.BooleanOptionalAction)
args = arg.parse_args()
installLocation = input("Enter The Location Where You Want To Install PCC to: ")#

def DownloadGCC():
    print("Downloading Will Start Soon")
    url = ("https://github.com/brechtsanders/winlibs_mingw/releases/download/13.2.0posix-17.0.6-11.0.1-ucrt-r5/winlibs-x86_64-posix-seh-gcc-13.2.0-mingw-w64ucrt-11.0.1-r5.zip")
    filename = tempfile.gettempdir() + "/gcc.zip"
    a, headers = urlretrieve(url, filename)
    print(headers["Content-Length"])
    print(f"Downloading G++ zip file to temp, Size: {round(((int(headers["Content-Length"]) / 1024) / 1024), 2)} MB ")
    
    urlretrieve(url, filename)
    print("Downloading Finished")

def UnzipGCC():
    print(f"Extracting G++ To {installLocation}/g++_install/")
    path = tempfile.gettempdir() + "/g++.zip"
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
    url_h = (f"https://raw.githubusercontent.com/Bloodstone2179/PCC/master/SRC/builtins.h")
    url_pcc = (f"https://raw.githubusercontent.com/Bloodstone2179/PCC/master/Releases/Win64/{y["LatestReleaseVersion"]}/pcc.exe")
    url_pcc_u = (f"https://raw.githubusercontent.com/Bloodstone2179/PCC/master/Releases/Win64/pcc_installer.exe")
    filename_pcc = installLocation + "/pcc.exe"
    filename_pcc_u = installLocation + "/pcc_updater.exe"
    if os.path.exists(filename_pcc_u) is not True:
        urlretrieve(url_pcc_u, filename_pcc_u)
    filename_h = installLocation + "/g++_install/mingw64/include/c++/13.2.0/builtins.h"
    urlretrieve(url_pcc, filename_pcc)
    urlretrieve(url_h, filename_h)
    
    print("PCC Finshed Downloading\nEverything Is Now Installed")

if args.update == True:
    DownloadPCC()
if args.testing == False and args.update == False:
    DownloadGCC()
    UnzipGCC()
    DownloadPCC()
if args.testing == True:
    #copy over the builtins file and the built exe to replace the 1 in install location
    y = json.loads(open("/AQA PseudoCode transpiler/VersionFile.json").read())
    print(y["LatestReleaseVersion"])
    currentversion = y["LatestReleaseVersion"]
    pccDevLocation = getcwd() + "/AQA PseudoCode transpiler/Releases/Win64/" + currentversion
    shutil.copyfile(pccDevLocation + "/pcc.exe", installLocation + "/pcc.exe")
    shutil.copyfile(getcwd() + "\\AQA PseudoCode transpiler\\SRC\\builtins.h", installLocation + "/g++_install/mingw64/include/c++/13.2.0/builtins.h")
    print(pccDevLocation)
    