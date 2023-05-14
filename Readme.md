# Raspberry Pi Pico 433MHz Remote Emulator (MicroPython)

This repository contains a MicroPython project for the Raspberry Pi Pico board that emulates a 433MHz remote control. The remote control is designed to turn on and off a Steffen power remote plug. With this project, you can control the power plug using the Raspberry Pi Pico over WiFi.

## Hardware

- Raspberry Pi Pico (W)
- [Steffen power remote plug](https://cdn.competec.ch/images2/9/7/7/201756779/201756779_xxl3.jpg)
- [433MHz transmitter module](https://cdn-reichelt.de/bilder/web/xxl_ws/A300/DEBO_433_RX-TX.png)

## Usage

1. Clone this repository:
2. Connect the 433MHz transmitter module to the Raspberry Pi Pico as follows:
- Connect the VCC pin of the transmitter module to the 3.3V pin
- Connect the GND pin of the transmitter module to any GND pin
- Connect the DATA pin of the transmitter module to GPIO26 on
3. Connect your Raspberry Pi Pico to your computer using a USB cable and upload the files in the `firmware` folder to the board.
4. Send on/off signal on a specific channel by calling the `send_signal` function in the `main.py` file.

## License

This project is licensed under the [MIT License](LICENSE).