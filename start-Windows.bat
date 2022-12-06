@echo off

cls
echo Installing requirements...
pip install -r ./requirements.txt
pip install -r ./requirements_uncertain.txt

cls
python "./Downloader Menu.py"

pause