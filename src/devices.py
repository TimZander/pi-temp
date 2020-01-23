import glob

class Device:
    def __init__(self, path, serial):
        self.path = path
        self.serial = serial

def get_devices(folder, slave_path, matching_string):
    device_folder = glob.glob(base_dir + matching_string)
    devices = []
    for folder in device_folder:
        devices.append(Device(folder + slave_path, get_device_serial(folder, base_dir)))
    return devices


def get_device_serial(device_folder, base_dir):
    return device_folder.replace(base_dir, '')
