# balronu

Open Source für Home Assistant mit Schwerpunkt auf Mobilität, Wohnmobil,
Routenplanung, Flugverkehr und Wetter.

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Integrationen-41bdf5?logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Dokumentation](https://img.shields.io/badge/Dokumentation-Deutsch%20%7C%20English-2f855a)](README.en.md)

## Projekte

Die folgenden fünf Projekte werden eigenständig entwickelt. Gemeinsame
Dashboard-Einbindung oder optionale Schnittstellen machen sie nicht zu einem
einzigen Projekt.

| Projekt | Kurzbeschreibung | Stand |
| --- | --- | --- |
| [Mobile Fuel Stations](https://github.com/balronu/ha-mobile-fuel-stations) | GPS-basierte Tankstellensuche, Preisvergleich und Navigation für Home Assistant. | Stable `v0.6.1`; Beta `v0.7.0-beta.6` |
| [Air Traffic](https://github.com/balronu/ha-air-traffic) | Flugzeugdaten und Kartenvisualisierung in Home Assistant; die frühere Merge Card ist integriert. | Stable `v1.3.1`; Beta `v1.4.0-beta.1` |
| [Camper Travel Journal](https://github.com/balronu/ha-camper-travel-journal) | GPS-basiertes Reisetagebuch mit Reisen, Fahrten, Historie, Kosten, GPX-Import und PDF-Berichten. | Stable `v0.2.0` |
| [Bike Weather](https://github.com/balronu/ha-bike-weather) | Fahrradwetter, Tourenplanung, regelmäßige Fahrten, Morgenprognose und eigene Lovelace-Karte. | Stable `v0.3.1` |
| [Camper Route Planner](https://github.com/balronu/ha-camper-route-planner) | Wohnmobil-Routenplanung mit Fahrzeugprofilen, interaktiver Karte, gespeicherten Routen und GPX-Export. | **In Entwicklung – noch kein veröffentlichtes Release** |

Stable- und Beta-Angaben entsprechen den aktuell veröffentlichten GitHub-
Releases. Geplante Funktionen sind ausdrücklich als geplant beziehungsweise
in Entwicklung gekennzeichnet.

Camper Travel Journal, Mobile Fuel Stations und Camper Route Planner können
optional in ein Wohnmobil-Dashboard eingebunden werden. Sie bleiben getrennte
Entwicklungen mit eigenen Repositories, Releases und Installationshinweisen.

## Technische Schwerpunkte

- Home-Assistant-Custom-Integrationen und Config-/Options-Flows
- HACS-kompatible Pakete und integrierte Lovelace-Karten
- GPS-, Wetter-, Flugverkehrs- und Kraftstoffdaten
- robuste Aktualisierung, Datenvalidierung und nachvollziehbare Zustände
- deutschsprachige Dokumentation mit englischer Ergänzung, wo sie sinnvoll ist

## Zusammenarbeit und Hinweise

Fehlerberichte, Fragen und Verbesserungsvorschläge sind in den jeweiligen
Repositories willkommen. Bitte vor dem Erstellen eines Issues die vorhandene
Dokumentation und die Issue-Vorlagen lesen und möglichst Home-Assistant-
Version, Integrationsversion sowie reproduzierbare Schritte angeben.

- [Alle öffentlichen Repositories](https://github.com/balronu?tab=repositories)
- [Mobile Fuel Stations – Issues](https://github.com/balronu/ha-mobile-fuel-stations/issues)
- [Air Traffic – Issues](https://github.com/balronu/ha-air-traffic/issues)
- [Camper Travel Journal – Issues](https://github.com/balronu/ha-camper-travel-journal/issues)
- [Bike Weather – Issues](https://github.com/balronu/ha-bike-weather/issues)
- [Camper Route Planner – Issues](https://github.com/balronu/ha-camper-route-planner/issues)
- [Englische Profilversion](README.en.md)

## Hinweis zur alten Air-Traffic-Merge-Card

Die frühere [separate Merge Card](https://github.com/balronu/air-traffic-merge-card)
bleibt als archiviertes Legacy-Projekt erhalten. Ihre Funktion ist in Air
Traffic integriert; der Legacy-Kartentyp bleibt für bestehende Installationen
kompatibel. Der Fork [brands](https://github.com/balronu/brands) ist kein
eigenständiges Home-Assistant-Projekt.
