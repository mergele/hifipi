# hifipi
Projektdokumentation für eine Musikbox mit einem Raspberrypi, Hifiberry AMP. Einbau zusammen mit Lautsprechern und Steuerelementen (Drehencoder für Lautstärke / Auswahl, Buttons für Steuerung)

## Material / Komponenten
* https://www.raspberrypi.org/products/raspberry-pi-3-model-b/, [amazon](https://www.amazon.de/Raspberry-Pi-Model-ARM-Cortex-A53-Bluetooth/dp/B01CD5VC92)
* https://www.hifiberry.com/products/ampplus/, https://www.amazon.de/gp/product/B076CFNC6Z, 
* https://www.amazon.de/gp/product/B076CFNC6Z/
* https://www.amazon.de/gp/product/B06XCSB9N3/
* Larcele 10 Stück 12mm Momentan Wasserdicht Push Button Mini DruckTaster Druckknopf ANKG-01 (Weiß), https://www.amazon.de/gp/product/B07DS9X9TX/
* Larcele 10 Stück 12mm Momentan Wasserdicht Push Button Mini DruckTaster Druckknopf ANKG-01 (Schwarz), https://www.amazon.de/gp/product/B01MRN1UCP
* Larcele 10 Stück 12mm Momentan Wasserdicht Push Button Mini DruckTaster Druckknopf ANKG-01 (5 Farben), https://www.amazon.de/gp/product/B06XCSB9N3/
* Hikig 5 Stück KY-040 Drehwinkelgeber Drehgeber Rotary Encoder Modul mit 15 x 16,5 mm mit Knauf Cap für Arduino (5er Pack) HKT1062, https://www.amazon.de/gp/product/B07D356LRH/
* KFD Netzteil 18V 3,33a Ladegerät für Beats by Dr. Dre Tragbarer BeatBox Mobiler Wireless Portable Bluetooth Lautsprecher Speaker Harman Kardon BSC60-180333 700-0097-001 810-00052-00 777-00012-00-A 777-00010-00-B Power Supply, https://www.amazon.de/gp/product/B01E3XJOH4


## RaspberryPi 
### Installation
### Basis Setup
sudo raspi-config
 Localisation Options
  Change Locale, add  de_DE.UTF-8 UTF-8, set it as default
 Set Timezone  


sudo apt update && sudo apt upgrade -y
sudo apt install tmux mc 
sudo apt install git   
### MPD

### AMP+

### Python Control Script
#### Encoder
Inbetriebnahme mit dem Script von https://www.stuffaboutcode.com/2015/05/raspberry-pi-and-ky040-rotary-encoder.html, test-encoder.py
   
## Gehäuse / Holzarbeiten

## Quellen / Inspiration / ... 
* Checking Raspberry Pi Board Version https://www.raspberrypi-spy.co.uk/2012/09/checking-your-raspberry-pi-board-version/
* Github Markdown Cheatsheet, https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* GPIO Layout, https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png

---
## MISC
Sammlung sonstiger Links / Quellen / Anleitungen / ...
* Inbetriebnahme Encoder KY 040 https://github.com/martinohanlon/KY040
* https://volumio.org/forum/gpio-pins-control-volume-t2219.html
* https://forum-raspberrypi.de/forum/thread/16127-volumio-mit-taster-steuern/
* https://support.hifiberry.com/hc/en-us/community/posts/201843611-Hardware-Volume-Control#post-17420
* MPD, http://manpages.ubuntu.com/manpages/precise/en/man1/mpc.1.html
* MPD, https://www.musicpd.org/doc/html/protocol.html
* MPD, https://mpd.fandom.com/wiki/Clients
* MPD, https://www.raspberrypi.org/forums/viewtopic.php?t=74466
* VOLUMIO, https://nanomesher.com/use-as-volumio-control/
* GPIO, https://sourceforge.net/projects/raspberry-gpio-python/
* GPIO, https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png
* ENCODER, https://www.adafruit.com/product/377
* https://volumio.org/forum/getting-rotary-encoder-working-t9690.html
* https://www.ebay.de/itm/Drehregler-KY-040-Rotary-Encoder-Drehgeber-Taster-Poti-Arduino-Raspberry-Pi-/162961349697
* http://www.linkerkit.de/index.php?title=KY-040_Kodierter_Drehschalter_%28Rotary_Encoder%29
* https://www.stuffaboutcode.com/2015/05/raspberry-pi-and-ky040-rotary-encoder.html
* MISC, https://volumio.org/forum/interface-with-gpio-and-rs232-spi-t2192.html
* https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
* HIFIBERRY Forum, 
* HIFIBERRY Forum, https://www.hifiberry.com/build/documentation/gpio-usage-of-hifiberry-boards/
* HIFIBERRY Forum, https://support.hifiberry.com/hc/en-us/community/posts/201492812-free-Pins-GPIO-Amp-for-Ver-A-B-
* HIFIBERRY Forum, https://support.hifiberry.com/hc/en-us/community/posts/201494692-Woodware
* HIFIBERRY Forum, https://support.hifiberry.com/hc/en-us/community/posts/360000691765-New-Hifiberry-project-with-AMP2
* HIFIBERRY Forum, https://support.hifiberry.com/hc/en-us/community/posts/201843611-Hardware-Volume-Control#post-17420
* HIFIBERRY Forum, https://support.hifiberry.com/hc/en-us/community/posts/201494692-Woodware?page=2#comments
* HIFIBERRY Forum, https://support.hifiberry.com/hc/en-us/community/posts/205753859-Amp-Hardware-Volume-Control-
* http://www.iknowthe.net/blog/raspberry-pi-volumio-song-gpio-button.html
