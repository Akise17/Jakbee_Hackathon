from mlx90614 import MLX90614

thermometer_address = 0x5a

while True:
    thermometer = MLX90614(thermometer_address)

#     print(thermometer.get_amb_temp())
    print(thermometer.get_obj_temp())

pip3 install PyMLX90614
sudo modprobe i2c_bcm2708
sudo su -c 'echo "Y" > /sys/module/i2c_bcm2708/parameters/combined'