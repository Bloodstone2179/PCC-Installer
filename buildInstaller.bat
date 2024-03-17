@echo off
pyinstaller --noconfirm --onefile --console --distpath "../AQA PseudoCode transpiler/Releases/Win64" --name "pcc_installer" --clean "main.py"
python moveFiles.py