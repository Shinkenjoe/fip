Feature: Es können WZP-Daten eingegeben und gespeichert werden

Edith ist eine Benutzerin

Scenario: Eingabe Seite
  Given Edith besucht die Eingangsseite
  When Edith zur Eingabeseite wechselt
  Then erscheint ein Formular mit Eingabeboxen mit der ID "Feld"
  | besitzer        |
  | revier          |
  | distrikt        |
  | abteilung       |
  | bestand         |
  | wzp_nummer      |
  | hangausrichtung |
  | hangneigung     |
  | klasse          |
  | baumart         |
  | durchmesser     |
  | hoehe           |
  | grundflaeche    |
  | vitalitaet      |
  | qualitaet       |
  | alter           |
