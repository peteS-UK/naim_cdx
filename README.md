# Naim CDX Integration for Home Assistant

A simple media player to control a Naim CDX CD player from Home Assistant. Since the CDX has no network control, this integration sends its RC5 infrared commands through Home Assistant's Core Infrared integration, which must be setup with a compatible emitter integration prior to installation.

Existing installations using a Broadlink or Tuya remote must configure an infrared emitter and complete the Select an infrared emitter repair. Until it is completed, the media player is unavailable and cannot send commands.

## Installation

The preferred installation approach is via Home Assistant Community Store - aka [HACS](https://hacs.xyz/). The [repo](https://github.com/peteS-UK/naim_cdx) is installable as a [Custom Repo](https://hacs.xyz/docs/faq/custom_repositories) via HACS.

If you want to download the integration manually, create a new folder called naim_cdx under your custom_components folder in your config folder. If the custom_components folder doesn't exist, create it first. Once created, download the files and folders from the [github repo](https://github.com/peteS-UK/naim_cdx/tree/main/custom_components/naim_cdx) into this new naim_cdx folder.

Once downloaded either via HACS or manually, restart your Home Assistant server.

## Configuration

Configuration is done through the Home Assistant UI.  Once you're installed the integration, go into your Integrations (under Settings, Devices & Services), select Add Integration, and choose the NAIM CDX integration, or click the shortcut button below (requires My Homeassistant configured).

[![Add Integration to your Home Assistant
instance.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=naim_cdx)

This will display the configuration page
