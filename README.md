# PC Nano Relay Power Supply

This project is a simple Arduino Nano sketch that demonstrates basic relay control and LED status output. It is intended as a starting point for a PC power-control system, but the current version does not yet communicate with a Sonoff device or process external commands.

## How the program works

When the Arduino starts, the program initializes the serial monitor at 9600 baud and prints the word "Start".

In the setup phase:
- Pin 5 is configured as an output for the relay.
- Pins 12, 11, and 10 are configured as outputs for three LEDs.
- The relay is briefly activated at startup: it is set LOW for 500 ms and then HIGH again.

In the main loop:
- All three LEDs are turned ON together for 1 second.
- Then all three LEDs are turned OFF for 1 second.
- This creates a simple blinking pattern that can be used as a visual indicator during testing.

## Pin assignments

- Pin 5: relay control
- Pin 12: LED 1
- Pin 11: LED 2
- Pin 10: LED 3

## What this means in practice

The sketch currently behaves like a basic hardware test and prototype example. It confirms that the relay and LEDs can be controlled by the Arduino. In a later version, this logic can be expanded so that a Sonoff switch, Alexa command, or other trigger activates the relay to power on a desktop PC.

## Safety note

If this project is later adapted to switch real PC power, use a safe and properly isolated circuit. Do not connect mains voltage directly to the Arduino or relay module without appropriate protection and wiring design.

