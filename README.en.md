# balronu

Open source Home Assistant projects focused on mobility, motorhomes, route
planning, air traffic and weather.

[Website: smartcamper765.de](https://www.smartcamper765.de)

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Open%20Source-41bdf5?logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Documentation](https://img.shields.io/badge/Documentation-English%20%7C%20Deutsch-2f855a)](README.md)

## Projects

The following six projects are developed independently. Shared dashboard
integration or optional interfaces do not turn them into one project.

| Project | Description | Development status |
| --- | --- | --- |
| [Mobile Fuel Stations](https://github.com/balronu/ha-mobile-fuel-stations) | Home Assistant integration for fuel stations and fuel prices with GPS-based provider selection, fallback, quota diagnostics, multiple vehicles, and a dedicated Lovelace card. | Stable [`v0.8.7`](https://github.com/balronu/ha-mobile-fuel-stations/releases/tag/v0.8.7) |
| [Air Traffic](https://github.com/balronu/ha-air-traffic) | Aircraft data and map visualization in Home Assistant; the former Merge Card is integrated. | Stable [`v1.3.1`](https://github.com/balronu/ha-air-traffic/releases/tag/v1.3.1); beta [`v1.4.0-beta.1`](https://github.com/balronu/ha-air-traffic/releases/tag/v1.4.0-beta.1) |
| [Camper Travel Journal](https://github.com/balronu/ha-camper-travel-journal) | Privacy-conscious Home Assistant travel journal with trips, drives, expenses, GPX import, place resolution, Lovelace cards and offline PDF reports. | Stable [`v0.4.1`](https://github.com/balronu/ha-camper-travel-journal/releases/tag/v0.4.1) |
| [Bike Weather](https://github.com/balronu/ha-bike-weather) | Cycling weather, ride planning, regular rides, tomorrow forecast and a dedicated Lovelace card. | Stable [`v0.3.1`](https://github.com/balronu/ha-bike-weather/releases/tag/v0.3.1) |
| [Camper Weather](https://github.com/balronu/ha-camper-weather) | Weather, camping and outdoor assistant for motorhomes with Open-Meteo, warnings, camping score and a dedicated Lovelace card. | Stable [`v0.1.3`](https://github.com/balronu/ha-camper-weather/releases/tag/v0.1.3) |
| [Camper Route Planner](https://github.com/balronu/ha-camper-route-planner) | Motorhome route planning with vehicle profiles, an interactive map, saved routes and GPX export. | Stable [`v0.1.5`](https://github.com/balronu/ha-camper-route-planner/releases/tag/v0.1.5); beta [`v0.1.6-beta.10`](https://github.com/balronu/ha-camper-route-planner/releases/tag/v0.1.6-beta.10) |

Stable labels reflect currently published GitHub releases. Planned features
are explicitly marked as planned or in development.

Mobile Fuel Stations supports Tankerkönig, Nakordoni and Petromap, with
highlights for the nearest and cheapest station. v0.8.7 is a maintenance release
without functional changes; the existing provider-specific
availability, fallback and quota diagnostics, automatic and manual fetch modes,
and persisted cache and GPS-country context. Data availability, market
permissions and address detail still depend on the respective provider.

Camper Travel Journal, Mobile Fuel Stations and Camper Route Planner can be
combined optionally in a motorhome dashboard. They remain separate projects
with their own repositories, releases and installation instructions.

## Shared focus

- Home Assistant custom integrations and responsive Lovelace cards
- GPS, fuel, weather and air-traffic data
- Privacy-aware local storage and explainable state
- German-first documentation with an English counterpart

## Notes

The former [Air Traffic Merge Card](https://github.com/balronu/air-traffic-merge-card)
remains available as an archived legacy project. Its functionality is
integrated into Air Traffic, while the legacy card type remains compatible with
existing installations. The [brands fork](https://github.com/balronu/brands) is
not presented as a standalone Home Assistant project.

See the [German profile version](README.md) and the
[public repositories](https://github.com/balronu?tab=repositories) for details.
