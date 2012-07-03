# Win/Win Strategie
## Übersicht
Programm zur Berechnung von heuristischen Lösungen für das Traveling Salesman Problem und das Hamiltonpfad Problem.

## Voraussetzung
Folgende Voraussetzungen müssen erfüllt sein, damit das Programm ausgeführt werden kann.

### Python
Um das Programm ausführen zu können, muss Python (inkl. argparse) installiert sein.

Archlinux:
	
	$ pacman -S python

Ubuntu:
	
	$ sudo apt-get install python3

	$ sudo apt-get install python3-setuptools

	$ easy_install3 argparse

### Blossom V
Zur Berechnung des perfekten Matchings wird der Blossom V Algorithmus benötigt.

	$ cd /tmp

	$ wget http://pub.ist.ac.at/~vnk/software/blossom5-v2.03.src.tar.gz

	$ tar xzf blossom5-v2.03.src.tar.gz

	$ cd blossom5-v2.03.src.tar.gz

	$ make

	$ cp blossom5 $WINWIN/src/bin

Wobei $WINWIN dem Wurzelverzeichnis der Win/Win Strategie entspricht.

## Ausführen des Programms
Das Programm kann auf der Kommandozeile ausgeführt werden. Dazu in den Ordner src wechseln und beispielsweise folgenden Befehl eingeben:

./bin/winwin -f data/in/christofides.tsp -s 1 -t 39 -ot 7798 -oh 7490

-f: Input File
-s: Startknoten für HPP 
-t: Zielknoten für HPP 
-ot: Länger der optimalen TSP Lösung
-oh: Länge der optimalen HPP Lösung
