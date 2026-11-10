# Naim CDX Integration for Home Assistant

[![Available in Marketplace](https://img.shields.io/badge/Marketplace-Available-41BDF5)](#installation-with-marketplace)
[![maintained](https://img.shields.io/maintenance/yes/2026.svg)](#)
[![maintainer](https://img.shields.io/badge/maintainer-%20%40petes--UK-blue.svg)](#)
[![version](https://img.shields.io/github/v/release/peteS-UK/naim_cdx)](#)

A simple media player to control a Naim CDX CD player from Home Assistant. Since the CDX has no network control, this integration sends its RC5 infrared commands through Home Assistant's Core Infrared integration, which must be setup with a compatible emitter integration prior to installation.

Existing installations using a Broadlink or Tuya remote must configure an infrared emitter and complete the Select an infrared emitter repair. Until it is completed, the media player is unavailable and cannot send commands.

## Installation with Marketplace

The [Marketplace](https://www.home-assistant.io/integrations/marketplace/) is built into **Home Assistant 2026.11 and later**; no separate store installation is needed.

1. As an administrator, open **Settings → Marketplace** and accept its first-use notice if prompted.
2. Search for **Naim CDX** and open its page.
3. Choose **Install**, review the version, then confirm **Install**. Account setup opens when installation finishes; continue with [Configuration](#configuration). A fresh installation does not need a restart.

Existing HACS installations migrate automatically when you upgrade Home Assistant to 2026.11. Your installed integration and updates carry over; you do not need to reinstall it.

## Installation with HACS

For older versions of Home Assistant, you can install via Home Assistant Community Store - aka [HACS](https://hacs.xyz/).  Search for **Naim CDX** and install the integration.

## Manual Installation
If you want to download the integration manually, create a new folder called naim_cdx under your custom_components folder in your config folder.  If the custom_components folder doesn't exist, create it first.  Once created, download the files and folders from the [github repo](https://github.com/peteS-UK/naim_cdx/tree/main/custom_components/naim_cdx) into this new naim_cdx folder.

Once downloaded either via HACS or manually, restart your Home Assistant server.

## Configuration

Configuration is done through the Home Assistant UI.  If the configuration page isn't displayed automatically, for example after a Marketplace installation, once you're installed the integration go into your Integrations (under Settings, Devices & Services), select Add Integration, and choose the NAIM CDX integration, or click the shortcut button below (requires My Homeassistant configured).

[![Add Integration to your Home Assistant
instance.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=naim_cdx)

This will display the configuration page

<img width="732" height="452" alt="image" src="https://github.com/user-attachments/assets/44ac5cf9-11ed-408a-8ba2-f5ff25d435d8" />

## Options

To change the infrared emitter later, open the Naim CDX integration in **Settings > Devices & services** and select **Configure**.