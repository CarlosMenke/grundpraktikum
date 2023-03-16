
# Andreas notizen
- WICHTIG: Wie kann man den Fehler von der Digitalisierung bei der fourier Transformationn beachten?


# Aufbau & Durchführung

## Einzelnder Schwingkreis
- Kondensator in Reihe geschalten mit Spule
- Spannungsquelle an Taster anschließen.
- Spannung Messen an Kondensator

## Gekoppelt mit Schwebung
- 1x Aufbau wie oben
- 1x Schwingkreis nur mit L und c

## Gekoppelt ohne schwebung
- Gemeinsame Spannungsquelle (???)

## Charakterisierung der Bauteile

- Großer Kondensator, mittlere Spule
- Messen von C und L mit dem Multimeter
- Frequenz überschlagen 1/sqrt(LC)

# Einzelner Schwingkreis
- Rauschmessung

- Sinnvolle Messparamete (Aus frequenz)
- Spannung abgreifen am Kondensator
- Daher schwingungsverlauf am Cassy
- FFT der schwingung wie wird da der Fehler berechnet?
- Messzeit optimieren
- Intervall:
- Messzeit: Sodass die Dämpfung noch keinen Signifikanten einfluss hat
- Trigger:
- Was ist unsere Erwartung?

- Einhüllende Anpassen, hier muss digitalisierungsfehler beachtet werden
- Wiederstand daraus bestimmen


# Gekoppelt mit Schwebung
- Fester Abstand (Abstan aufschreiben)
- Spannung an beiden Kondensatoren Messen
- Schwebungsfrequenz und Grundfrequenz Messen --> f- und f+ Berechnen
- Verschiebung von Maximum der Schwebung 1 zum Maximum der Schwebung 2
- f- und f+ sinf abhängig von der Kopplung
- Abstand Also kopplung Variieren
- Spulen auf eisenkern Montieren

- Digitalisierungsfehler hat keinen einfluss auf Frequenz
- Wie ändert sich die kopplung abhängig vom Abstand
- Fit anpassen mit d^a


# Gekoppelt one Schwebung (gleichsinnige und Gegensinnige Anregung)
- Schalte ist ein Schalter mit mehreren Schaltern, Spannungsquelle an diesen Anschließen
- Gleichsinnige Anregung:
    - F+, ist die Frequenz die wir am Kondensator Messen können.
    - Unterschied zwischen den Beiden Schwingkreisen?
- Gegensinnige Anregung
    - F- ist größer als F+
- Fourierspektren der Beiden Messungen gibt die Frequenzen
- Mit F+ und F- k berechnen

# Messanzahl
- 10x Messung pro Aufbau

# Auswertung
- Hauptwerkzeug ist die FFT
- Von dieser Müssen dann die Verschiedenen Peaks bestimmt werden
- !!! Fehler bei FFT !!!

# Fehler
- Digitalisierung CASSy
- Systematischer Fehler CASSY (Ableseungenauigkeit)
- Statistischer Fehler von Mehrfacher Messung
- Vernachlässigen des Wiederstands
- Fehler von Kapazitäts und Induktivität Bestimmung
