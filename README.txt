Win/Win Strategie
=================
Programm zur Berechnung von heuristischen Lösungen für das TSP/HPP.

Voraussetzung
=============
Um das Programm ausführen zu können, muss python (inkl. argparse) installiert sein.

Archlinux: 
sudo pacman -S python

Ubuntu: 
sudo apt-get install python3
sudo apt-get install python3-setuptools
sudo easy_install3 argparse

Nutzen der mitgelieferten VM
============================
Auf der DVD wird eine virtuelle Maschine mitgeliefert, die mit Virtualbox genutzt werden kann. Auf dieser Maschine ist die benötigte Software bereits installiert.

Archlinux:
sudo pacman -S virtualbox
sudo modprobe vboxdrv
Das Virtualbox module in der rc.conf eintragen, damit es bei jedem Neustart geladen wird: MODULES=(vboxdrv)

Ubuntu:
sudo apt-get install virtualbox-ose
sudo virtualbox-ose-qt

Wenn Virtualbox installiert ist, kann die virtuelle Maschine via "File" => "Import Application" importiert werden.

Ausführung des Programms
========================
Das Programm kann auf der Kommandozeile ausgeführt werden. Dazu in den Ordner src wechseln und beispielsweise folgenden Befehl eingeben:

./bin/winwin -f data/in/christofides.tsp -s 1 -t 39 -ot 7798 -oh 7490

-f: Input File
-s: Startknoten für HPP
-t: Zielknoten für HPP
-ot: Länger der optimalen TSP Lösung
-oh: Länge der optimalen HPP Lösung

Mögliche Problem:
=================
Permission Denied Fehler bei der Ausführung: Berechtigungen auf de auszuführenden Files sind falsch. In den Ordner bin wechseln und mit "chmod 755 *" die Berechtigungen neu setzen.

Fehler beim ausführen von blossom5. Die kombilierte Version ist nicht mit Ihrem Betriebssystem kompatibel. Das Programm muss neu kompiliert werden:

In den Ordner tmp wechseln:
cd /tmp

Archiv herunterladen:
wget http://pub.ist.ac.at/~vnk/software/blossom5-v2.03.src.tar.gz

Archiv entpacken:
tar xzf blossom5-v2.03.src.tar.gz

In den Ordner blossom5-v2.03.src.tar.gz wechseln:
cd blossom5-v2.03.src.tar.gz

Das Makefile ausführen:
make

Datei in den bin Ordner kopieren, in dem sich die alte blossom5 Datei befindet
cp blossom5 ~/path/to/bin/
