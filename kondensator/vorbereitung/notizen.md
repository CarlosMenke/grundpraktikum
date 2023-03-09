## Fragen
- Resiuenplots mit syst. oder stat. Fehler dargestellt?
- X quadrat anpassung: Statistische oder Systematischen Fehler verwenden. 
    - oder summe von beiden?
- Im Resiuenplot: Nimmt man da die funktion, welche man aus der chi quadrat methode hat?
- Sind Spannung und Stromstärke korreliert?
- Können wir die Messwerte auch linarisieren, und dann mit der Chiquadrat methode die linare funktion bestimmen?
- wie bestimmt man auf die paramerter der linaren regresson die unsicherheiten schärtzen
- Müssen wir die Methode der effektieven Varianz verwenden? Da unser x nur einen systematischen digitalisierungs fehler haben.
- Sollen wir die qualität der Anpassung mit der Pull Methode bestimmen?



## Durchführung

!!!Messung wiederstan mit gleichen Eistellungen wie Kondensator!!!

### Vorversuch bestimmung des Wiederstands

- Bestimmung des wiederstands mit CASSY

- Aufbau der Schaltung
    - Siehe Gerätekund Aufbau.
- Maximale Spannung die angelegt werden darf bestimmen (P = UI => P = RI^2)
    - Maximale Leistung für Cassy ist P = 3.2W (Aus Cassy Daten berechnet)
    - => I = sqrt(P/R) = 0.178 A
    - bei 2W wiederstand =>
- Führen Messung 10x Durch
- Stelle Spannung Digital ein, umd schalte diese an zu Durchführung der Messung
    - ( Spannugn ein aus schalten wärend einer Messung?)
- lineare Regression an werte anpassen
- Aus Steigung kann der Wiederstand berechnet werden
- Systematischer Messfehler:
    - Digitalisierung
    - Abtastrate auf x-achse
    - Fortpflanzen von diesem Fehler auf R
- Stat. Messfehler:
    - Stat. schwankung der Messung vom realen wert. (Berechnen aus einem Datenpunkt (z.b. 3V) aus 10x Messung )
        - Durch festhalten von U Fehler von I berechnen, und umgekehrt?
    - hier muss die Korrelation beachtet werden?
- Verschiebmethode

### Bestimmen Kondensator mit Osziloskop

- Schaltbild in Aufgabenstellung
- Eistellen von Messwerterfassungseinstellungen
    - überschlagen der Zeitkonstante
- Bilder Vom Osziloskop speichern!!
- Ablesen von Spannungspaaren uund Zeitpaaren = wie ablesen von Zeitkonstante?
    - diese Müssen gespeichert werden ( Tabelarisch oder mit Bild)
    - Mit umgestellter Formel kann Kapazität bestimmt werden ( Zeitkonstante)
- Pro Koondensator 5x Aufladen und Entladen
    - Jedes mal mit cursor ablesen (?) Immer in gleicher Position (?)
- Masse des Osziloskops muss zwischen strom und Wiederstand geschaltet werden.
- Bei Aufladung Strom Messen
- Bei entladung Spannung Messen

### Bestimmung Kondensator mit CASSY

- Taster verwenden um auflade bzw. entladevorgang zu starten
- Wähle Messbereich Identisch zu Wiederstandsmessung
- Darstellung im CASSY logarythmieren
- Statistische Fehler auf U und I für alle messpunkte gleich?


## Messparametereinstellung

- Abtastrate: mit ta = CR => ta = 500 mu_s => Abtastrate 1mu_s
- Messintervall: 10 mu_s etspricht 20x ta
- Trigger:
    - entladen: Fallenden Flanke, Spannung knap unter Umax
    - laden: Steigende Flanke, Knap über 0V
- Spannungsbereich: Abhängig von Leistungsgrenze Wiederstand





