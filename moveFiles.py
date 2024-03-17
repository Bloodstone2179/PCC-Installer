import shutil
from os import getcwd
installLocation = input("Enter PCC Install Location: ")
pccDevLocation = getcwd() + "//../AQA PseudoCode transpiler/Releases/Win64/"
pcc_installer = pccDevLocation + "pcc_installer.exe"

shutil.copyfile(pcc_installer, installLocation + "/pcc_updater.exe")