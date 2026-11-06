# Naim CDX Integration for Home Assistant

A simple media player to control a Naim CDX CD player from Home Assistant. Since the CDX has no network control, this integration sends its RC5 infrared commands through Home Assistant's Core Infrared integration.

## Installation

The preferred installation approach is via Home Assistant Community Store - aka [HACS](https://hacs.xyz/). The [repo](https://github.com/peteS-UK/naim_cdx) is installable as a [Custom Repo](https://hacs.xyz/docs/faq/custom_repositories) via HACS.

If you want to download the integration manually, create a new folder called naim_cdx under your custom_components folder in your config folder. If the custom_components folder doesn't exist, create it first. Once created, download the files and folders from the [github repo](https://github.com/peteS-UK/naim_cdx/tree/main/custom_components/naim_cdx) into this new naim_cdx folder.

Once downloaded either via HACS or manually, restart your Home Assistant server. Set up a supported infrared emitter in Home Assistant before adding the integration, then select that emitter in the Naim CDX setup flow.
