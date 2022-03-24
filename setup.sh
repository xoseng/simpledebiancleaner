#!/bin/bash
# Autor: Xose
# Require root for running the script
# NOTICE: Comment with # the line 59 (rm -rf $SCRIPT) if you want don't delete this setup file

if [ "`id -u`" != 0 ] ;
        then
            echo -e "\n"
            clear
            echo "It requires root to run the script."
            echo "Abort, press any key to continue..."
            read abort
            clear
            exit 1
fi
#first install requirements

apt-get install python3 -y
apt-get install python3-pil python3-pil.imagetk -y
apt-get install python3-tk -y
apt-get install wget -y
apt-get install zip -y

SCRIPT=$(readlink -f $0);

cd /tmp/
wget https://github.com/xoseng/simpledebiancleaner/archive/master.zip
unzip master.zip
rm master.zip
mv simpledebiancleaner-master /opt/simpledebiancleaner

echo "#!/bin/bash" > run.sh
echo "gnome-terminal -x /opt/simpledebiancleaner/simpledebiancleaner.sh" >> run.sh

echo "#!/bin/bash" > simpledebiancleaner.sh
echo "cd /opt/simpledebiancleaner/" >> simpledebiancleaner.sh
echo "sudo python3 simpledebiancleaner.py" >> simpledebiancleaner.sh
echo "exit" >> simpledebiancleaner.sh

#create dektop entry
echo "[Desktop Entry]" > simpledebiancleaner.txt
echo "Type=Application" >> simpledebiancleaner.txt
echo "Name=Simple Debian Cleaner" >> simpledebiancleaner.txt
echo "Comment=System clean tool" >> simpledebiancleaner.txt
echo "Icon=/opt/simpledebiancleaner/img/logo_ico.png" >> simpledebiancleaner.txt
echo 'Exec="/opt/simpledebiancleaner/./run.sh"'>> simpledebiancleaner.txt
echo "Categories=System utilities;" >> simpledebiancleaner.txt
echo "Path=/opt/simpledebiancleaner/" >> simpledebiancleaner.txt

chmod +x simpledebiancleaner.sh
chmod +x run.sh

mv simpledebiancleaner.sh /opt/simpledebiancleaner/
mv run.sh /opt/simpledebiancleaner/
mv simpledebiancleaner.txt /usr/share/applications/simpledebiancleaner.desktop

clear
echo "Done, press any key to exit..."
read exitp
rm -rf $SCRIPT
exit
