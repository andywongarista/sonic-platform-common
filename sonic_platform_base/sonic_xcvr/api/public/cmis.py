
"""
    cmis.py

    Implementation of XcvrApi that corresponds to CMIS
"""

from ...fields import consts
from ..xcvr_api import XcvrApi

class CmisApi(XcvrApi):
    NUM_CHANNELS = 8

    def __init__(self, xcvr_eeprom):
        super(CmisApi, self).__init__(xcvr_eeprom)

    def get_model(self):
        return self.xcvr_eeprom.read(consts.VENDOR_PART_NO_FIELD)

    def get_transceiver_info(self):
        admin_info = self.xcvr_eeprom.read(consts.ADMIN_INFO_FIELD)
        if admin_info is None:
            return None

        # TODO: Add the other xcvr info fields
        xcvr_info = {
            "type": admin_info[consts.ID_FIELD],
            "type_abbrv_name": admin_info[consts.ID_ABBRV_FIELD],
        }
        return xcvr_info

    def get_temperature(self):
        temp = self.xcvr_eeprom.read(consts.TEMPERATURE_FIELD)
        if temp is None:
            return None
        return float("{:.3f}".format(temp))
 
    def get_voltage(self):
        voltage = self.xcvr_eeprom.read(consts.VOLTAGE_FIELD)
        if voltage is None:
            return None
        return float("{:.3f}".format(voltage))

    def get_paging(self):
        return self.xcvr_eeprom.read(consts.FLAT_MEM_FIELD)
 
    def get_temperature_support(self):
        return self.get_paging()

    def get_voltage_support(self):
        return self.get_paging()