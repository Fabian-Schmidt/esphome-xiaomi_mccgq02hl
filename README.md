# Xiaomi door &amp; windows sensor 2 (MCCGQ02HL)

Xiaomi door &amp; windows sensor 2 (MCCGQ02HL)

Adopted from <https://github.com/esphome/esphome/pull/4605>. Changes:

- Removed esphome core change so it can be used as external component.
- Reorganize code to have ble and sensor in seperate nodes.

```yaml
external_components:
  - source: github://Fabian-Schmidt/esphome-xiaomi_mccgq02hl
    components: [ xiaomi_ble, xiaomi_mccgq02hl ]

esp32_ble_tracker:

xiaomi_mccgq02hl:
  - id: window_one
    mac_address: "E4:AA:EC:4E:5E:E4"
    bindkey: "e05552dabf6c7fa69010076c5855060b"

binary_sensor:
  - platform: xiaomi_mccgq02hl
    id: window_one
    light:
      name: "Mi Window Sensor Light"
    open:
      name: "Mi Window Sensor Open"

sensor:
  - platform: xiaomi_mccgq02hl
    id: window_one
    battery_level:
      name: "Mi Window Sensor Battery Level"
```

## Tweaking Bluetooth

Using the following config I was able to receive more often data from the sensor:

```yaml
esp32_ble_tracker:
  scan_parameters:
    interval: 10ms
    window: 10ms
    active: false
```
