FROM networktocode/nautobot:1.4.2-py3.9

RUN pip install --no-warn-script-location git+https://github.com/adrydale/nautobot_plugin_example

# docker build --no-cache -t adrydale/nautobot:1.4.2-py3.9 .
