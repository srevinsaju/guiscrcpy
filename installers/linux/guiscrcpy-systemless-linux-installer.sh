echo guiscrcpy : by srevinsaju
echo ===============================
echo       
echo Removing any instances of guiscrcpy from usr/local/bin
rm -f /usr/local/bin/guiscrcpy*
echo Copying new files
cp ./guiscrcpy*linux /usr/local/bin/
mv /usr/local/bin/guiscrcpy* /usr/local/bin/guiscrcpy
echo Making new directory guiscrcpy in /usr/share/guiscrcpy
mkdir /usr/share/guiscrcpy
echo Cleaning guiscrcpy in /usr/share/guiscrcpy
rm -rf /usr/share/guiscrcpy/*
echo Copying guiscrcpy_logo.png to /usr/share/guiscrcpy
cp -f guiscrcpy_logo.png /usr/share/guiscrcpy/
echo Removing any existence of guiscrcpy.desktop 
rm -rf /usr/share/applications/guiscrcpy*.desktop
echo Add Desktop Application launcher to App Menus
cp -f guiscrcpy.desktop /usr/share/applications/
echo Done...
echo Now you can launch guiscrcpy from your terminal by 
echo $ guiscrcpy
echo OR
echo from your Application Menu

