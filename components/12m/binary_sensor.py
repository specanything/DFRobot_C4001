import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import DEVICE_CLASS_MOTION
from . import CONF_DFRobot_C4001_ID, DFRobot_C4001Component

DEPENDENCIES = ["DFRobot_C4001"]

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema(
    device_class=DEVICE_CLASS_MOTION
).extend(
    {
        cv.GenerateID(CONF_DFRobot_C4001_ID): cv.use_id(DFRobot_C4001Component),
    }
)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_DFRobot_C4001_ID])
    binary_sens = await binary_sensor.new_binary_sensor(config)

    cg.add(parent.set_detected_binary_sensor(binary_sens))
