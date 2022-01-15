from digi.xbee.devices import DigiMeshDevice, RemoteXBeeDevice, XBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.packets.base import XBeePacket
from digi.xbee.models.mode import OperatingMode
import struct
import time

# Connect local device and open communication link 
device = DigiMeshDevice("/dev/ttyUSB0", 9600)
device.open()

# discover other devices on the network
network = device.get_network()
network.start_discovery_process()

while network.is_discovery_running(): 
    time.sleep(0.01)


devices = {dev.get_node_id():dev._64bit_addr for dev in network.get_devices()} # assign each node id with their respective 64 bit addr
devices[device.get_node_id()] = device._64bit_addr # assign the locally connected XBee to its 64 bit addr

print(devices)

# short demo but doesn't show on XCTU
# device2 = XBeeDevice("COM4",9600)
# device2.open()
# remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041C669D5"))
# device.send_data(remote_device, "Hello XBee!")

# basic but shows on XCTU
device.send_data_broadcast("Hello this is from GCS!")
device.close()


