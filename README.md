# Naim CDX Integration for Home Assistant

A simple media player to control Naim CDX CD player from Home Assistant. Since there's no direct control of the CDX, this uses a Broadlink or Tuya remote device to send the IR commands to the CDX.

## Installation

The preferred installation approach is via Home Assistant Community Store - aka [HACS](https://hacs.xyz/). The [repo](https://github.com/peteS-UK/naim_cdx) is installable as a [Custom Repo](https://hacs.xyz/docs/faq/custom_repositories) via HACS.

If you want to download the integration manually, create a new folder called naim_cdx under your custom_components folder in your config folder. If the custom_components folder doesn't exist, create it first. Once created, download the files and folders from the [github repo](https://github.com/peteS-UK/naim_cdx/tree/main/custom_components/naim_streamer) into this new naim_cdx folder.

Once downloaded either via HACS or manually, restart your Home Assistant server.
