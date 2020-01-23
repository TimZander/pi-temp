import devices

def test_get_serial():
    assert "serial" == devices.get_device_serial("test/serial", "test/")