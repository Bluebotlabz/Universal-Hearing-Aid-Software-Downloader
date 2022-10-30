@echo off

echo DISCLAIMER
echo I (Bluebotlabz), do not take any responsability for what you do using this software
echo All rights and credit go to their rightful owners. No copyright infringement intended.
echo.
echo Bluebotlabz and this downloader are not affiliated with or endorsed by any of the companies mentioned in this repository
echo Depending on how this software is used, it may breach the EULA of the downloaded software
echo This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited

echo.
echo.
echo.

echo Installing requirements...
pip3 install -r ./requirements.txt


:Menu
cls
echo.
echo.

echo ==================================================
echo =         Hearing Aid Software downloader        =
echo ========================================= v1.5.0 =
echo.
echo.
echo 1) Phonak Target Downloader
echo 2) Signia Connexx Downloader
echo 3) Oticon Genie 1 Downloader
echo 4) Oticon Genie 2 Downloader
echo 5) Unitron TrueFit Downloader
echo 6) Widex Compass GPS Downloader
echo 7) Bernafon OasisNXT Downloader

echo.
set /p SELECTION="Please choose a downloader to run (type the number you want): "

IF %SELECTION%==1 ( python "./Phonak Target Downloader.py" & GOTO Finished )
IF %SELECTION%==2 ( python "./Signia Connexx Downloader.py" & GOTO Finished )
IF %SELECTION%==3 ( python "./Oticon Genie 1 Downloader.py" & GOTO Finished )
IF %SELECTION%==4 ( python "./Oticon Genie 2 Downloader.py" & GOTO Finished )
IF %SELECTION%==5 ( python "./Unitron TrueFit.py" & GOTO Finished )
IF %SELECTION%==6 ( python "./Widex Compass GPS Downloader.py" & GOTO Finished )
IF %SELECTION%==7 ( python "./Bernafon OasisNXT Downloader.py" & GOTO Finished )

echo Invalid selection made, please try again
pause
GOTO Menu


:Finished
pause