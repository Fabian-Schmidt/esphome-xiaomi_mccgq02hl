import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import esp32_ble_tracker
from esphome.const import (
    CONF_MAC_ADDRESS,
    CONF_ID,
    CONF_BINDKEY,
)

AUTO_LOAD = ["xiaomi_ble"]
CODEOWNERS = ["@morph027", "Fabian-Schmidt"]
DEPENDENCIES = ["esp32_ble_tracker"]
MULTI_CONF = True

xiaomi_mccgq02hl_ns = cg.esphome_ns.namespace("xiaomi_mccgq02hl")
XiaomiMCCGQ02HL = xiaomi_mccgq02hl_ns.class_(
    "XiaomiMCCGQ02HL",
    esp32_ble_tracker.ESPBTDeviceListener,
    cg.Component,
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(XiaomiMCCGQ02HL),
            cv.Required(CONF_BINDKEY): cv.bind_key,
            cv.Required(CONF_MAC_ADDRESS): cv.mac_address,
        }
    )
    .extend(esp32_ble_tracker.ESP_BLE_DEVICE_SCHEMA)
    .extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await esp32_ble_tracker.register_ble_device(var, config)

    cg.add(var.set_address(config[CONF_MAC_ADDRESS].as_hex))
    cg.add(var.set_bindkey(config[CONF_BINDKEY]))
