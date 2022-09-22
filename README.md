# A Nautobot plugin example

This repo is a basic example for a Nautobot plugin. The examples are simple to keep the concepts straight forward.

# Installing

## Installing the library

On a Nautobot host, install this repo via pip:

`pip install --no-warn-script-location git+https://github.com/adrydale/nautobot_plugin_example`

In a Docker installation, a custom Docker image must be created using the dockerfile included in this repo.

**Important**: When installing the plugin, whether via a host install or a Docker install, all Nautobot instances must match (on the primary Nautobot instance and all worker nodes).

## Enabling the plugin in Nautobot

Usually all that is needed is to edit the `nautobot_config.py` configuration file. In that file, add `nautobo_plugin_example` to the `PLUGINS` definition.

```
PLUGINS = [
    'nautobot_plugin_example',
]
```

Nautobot documentation - [Installing and using plugins](https://nautobot.readthedocs.io/en/stable/plugins/#install-the-package)
