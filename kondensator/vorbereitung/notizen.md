- https://docplayer.org/27617886-Protokoll-zum-anfaengerpraktikum-physik-messung-von-kapazitaeten-auf-und-entladung-von-kondensatoren-sebastian-finkel-sebastian-wilken.html
 
## Fragen
- Resiuenplots mit syst. oder stat. Fehler dargestellt?
- X quadrat anpassung: Statistische oder Systematischen Fehler verwenden. 
    - oder summe von beiden?
- Im Resiuenplot: Nimmt man da die funktion, welche man aus der chi quadrat methode hat?
 
## Vorgespraech:
- Varianz bei chi quadrat ist n
- Bei verschiebe Methode: Statistische fehler ist der fehler fuer die verschobenen Werte
- statisticher Fehler auf den Einzelwert ist Fehler auf die Stromstärke beim Cassy (Wenn es keinne Trent gibt) (sigma gegn i vom wieder stand plotten)
- wenn man ln(i-ioff / i0) gegen t auftragt, ist die Unsicherheit sigma / I
- m ist -1/tau
- bei sigma symt ist nur 0.001 * I / sqrt(3), da der offset kürzt
- auch beim osziloskop gibt es einen offset: Rauschmessung
- tau = delta t / ln(u1 - uoff / u2 - uoff)
- delta U / sqrt(12) ist ablesegenauigkeit beim Osziloskop
- beim Osziloskop nehme ablesegenauigkeit als statistischen Fehler

 
    
 
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


### Notizen

sigma fehler auf den Einzelwert
Fehlerbalken:
    - Digitalisierungsfehler
    - statistischer Fehler auf U
    - x² wird immer schmaler desto mehr Messwerte man hat mit sqrt(f)
    - so oft messen, dass sigma (statistischer Fehler) kleiner als sigma_d (digitalisierungsfehler) ist
    - 10 Verschiedene Punkte
    - Residuen anschauen um systematik zu sehen und beurteilen ob gute Anpassung
    - fehler für lineare Regression ist immer statistischer Fehler
    - Spannungsgrenze berechnen mit max I von Cassy und max P von Wiederstand
    - Verwende statistischer Fehler auf den Einzelwert um fehler beim kondensator für lineare regression verwenden
    - Fehler nach ln mit gauß fehlerfortpflanzung berechnen
    - Was verwendet man für U0
    - Überprüfung x² und reisdudenplot plot
    - Ofset bestimmen mit Rauschmessung oder Asymtote
    - ln((I-I_of)/I)
    - systematischen fehler mit bereichsentwerte kürzt sich raus, bei der Verschiebmethode
    - U_o und I_off bestimmen
    - anhand des sprungs des cursors kann die genauigkeit dessen bestimmen ( 2 cursor punkte nebeneinander, dann d_U/sqrt(12))
        -statistisch fortplanzen
    - Jede kurve (Ladung entladung, strom Spannung) mindeststen 2x berechnen
    - Fehler auf R am Ende als systematischer Fehler

- Wiederstand bestimmen
    - wie oft messen? Spannung von 0 - 3V?
    - muss abtastrate als syst. Fehler berücksichtigt werden?
    - Wie bestimme ich den statistischen Fehler auf U, wenn ich u festhalte in der Messung?

- Beim Kondensator mit Osziloskop
    - Soll man mit dem Curosr mehr als einen Datenpunkt ablesen?
    - Sollen wir von allen Messungen ein Bild machen, oder reicht es sie in der Tabelle zu notieren?
    - Was ist die systematische Fehler beim Ablesen? =0 da wir mit dem Curosr ablese?
    - wie kommt man auf den statistischen fehler auf tau? Was meint ablese GEnauigkeit?
    - Weahle ein großes Tau

- CASSY Messung
    - Für den statistischen Fehler: Ist es leichter das Rauschen vom Wiederstand zu verwenden oder die Asymptote?
    - Was ist das Rauschen?
