from digi.xbee.devices import XBeeDevice
from digi.xbee.packets.base import XBeePacket
from digi.xbee.models.mode import OperatingMode
import struct
from XBeePacket import XBeePacket
from checksum import APIFrame

device1 = XBeeDevice("COM5", 9600)
device1.open()

# device1.send_data_broadcast("Hello")

# device1.close()

# data = struct.pack("2i?", 40, 26, True)
data = [2, 3, 4]
byte_array = bytearray(data)
print(byte_array)
# opMode = OperatingMode.ESCAPED_API_MODE

# packet = XBeePacket.create_packet(byte_array, opMode)

# cSum = packet.get_checksum()

# print(cSum)
testing2 = XBeePacket(2)
header = [0x83, 0x56, 0x78, 0x24, 0x00, 0x01, 0x02, 0x00, 0x03, 0xff, 0x85]
# packet = testing2.create_packet(header, 2)

checker = APIFrame(header)
checker.verify()
print(checker.verify)
