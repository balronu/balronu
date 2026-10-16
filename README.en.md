# balronu

Open source Home Assistant projects focused on mobility, motorhomes, route
planning, air traffic and weather.

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Open%20Source-41bdf5?logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Documentation](https://img.shields.io/badge/Documentation-English%20%7C%20Deutsch-2f855a)](README.md)

## Projects

The following five projects are developed independently. Shared dashboard
integration or optional interfaces do not turn them into one project.

| Project | Description | Development status |
| --- | --- | --- |
| [Mobile Fuel Stations](https://github.com/balronu/ha-mobile-fuel-stations) | GPS-based fuel-station search, fuel prices, multiple providers and a Lovelace card. | Stable `v0.6.1`; beta `v0.7.0-beta.6` |
| [Air Traffic](https://github.com/balronu/ha-air-traffic) | Aircraft data and map visualization in Home Assistant; the former Merge Card is integrated. | Stable `v1.3.1`; beta `v1.4.0-beta.1` |
| [Camper Travel Journal](https://github.com/balronu/ha-camper-travel-journal) | GPS-based travel journal with trips, drives, history, expenses, GPX import and PDF reports. | Stable `v0.2.0` |
| [Bike Weather](https://github.com/balronu/ha-bike-weather) | Cycling weather, ride planning, regular rides, tomorrow forecast and a dedicated Lovelace card. | Stable `v0.3.1` |
| [Camper Route Planner](https://github.com/balronu/ha-camper-route-planner) | Motorhome route planning with vehicle profiles, an interactive map, saved routes and GPX export. | **In development – no published release yet** |

Stable and beta labels reflect currently published GitHub releases. Planned
features are explicitly marked as planned or in development.

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
