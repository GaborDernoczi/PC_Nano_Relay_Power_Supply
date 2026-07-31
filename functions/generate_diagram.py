from PIL import Image, ImageDraw
from pathlib import Path

w, h = 1400, 900
img = Image.new('RGB', (w, h), 'white')
draw = ImageDraw.Draw(img)

draw.text((40, 25), 'Sonoff + Arduino Nano + Desktop PC Power Control', fill='black')

# Sonoff
sonoff = (80, 140, 330, 420)
draw.rounded_rectangle(sonoff, radius=20, fill='#f7f7f7', outline='black', width=3)
draw.text((110, 175), 'SONOFF', fill='black')
draw.text((100, 215), 'Smart Plug', fill='black')

# DC power supply
psu = (80, 480, 330, 680)
draw.rounded_rectangle(psu, radius=20, fill='#f7f7f7', outline='black', width=3)
draw.text((105, 515), 'DC Power', fill='black')
draw.text((115, 555), '5V / 12V', fill='black')

# Arduino Nano
nano = (430, 180, 780, 620)
draw.rounded_rectangle(nano, radius=20, fill='#f4f9ff', outline='black', width=3)
draw.text((490, 210), 'Arduino Nano', fill='black')
draw.text((500, 310), 'D5', fill='black')
draw.text((500, 350), 'GND', fill='black')
draw.text((500, 390), '5V', fill='black')

# Relay
relay = (860, 260, 1120, 500)
draw.rounded_rectangle(relay, radius=20, fill='#fff8d6', outline='black', width=3)
draw.text((900, 300), 'Relay Module', fill='black')
draw.text((900, 340), 'Switches PC', fill='black')

# PC
pc = (1240, 300, 1310, 500)
draw.rectangle(pc, outline='black', width=3)
draw.text((1260, 365), 'PC', fill='black')

# Wires
arrow_color = 'black'
draw.line((330, 250, 430, 250), fill=arrow_color, width=4)
draw.text((345, 225), 'Control signal', fill='black')
draw.line((330, 560, 430, 560), fill=arrow_color, width=4)
draw.text((340, 535), 'Power', fill='black')
draw.line((780, 400, 860, 400), fill=arrow_color, width=4)
draw.line((1120, 400, 1240, 400), fill=arrow_color, width=4)
draw.text((1140, 360), 'PC Power', fill='black')

draw.text((40, 760), 'Example wiring concept for remote PC power-on via Sonoff and Arduino Nano', fill='gray')

out = Path(__file__).with_name('diagram_sonoff_arduino_pc.jpg')
img.save(out, 'JPEG', quality=95)
print(out)
