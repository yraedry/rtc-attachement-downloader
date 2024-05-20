@ECHO OFF
echo "Add system variable"
setx C:\python\python.exe "%PATH%"
echo %PATH%

echo "installing requirements"
pip install -r requirements.txt
pause