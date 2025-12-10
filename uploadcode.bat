esptool --port COM7 erase_flash 
esptool --port COM7 --baud 460800 write_flash 0x1000 upython-20250911-v1.26.1.bin

ampy --port COM7 put src/main.py