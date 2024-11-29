# Klippy NTFY

> VERY MUCH USE AT YOUR OWN RISK. THIS IS A VERY SIMPLE EXTRA BUT IT'S MY FIRST ONE. YOU NEED A NTFY.SH OR SELF-HOSTED NTFY SERVER TO USE THIS. SETUP OF THAT IS OUT OF SCOPE OF THIS README.

> INSTRUCTIONS AND SETUP ARE STILL A WORK IN PROGRESS.

Ever want your 3D Printer to send you notifications right to your phone, computer or wherever?

Using a self-hosted ntfy server this plug in lets you do just that!
I haven't tested with the ntfy.sh service. So you're milage may very with that. I haven't implemented any of the ways to post to secure topics yet. I'm not likely to as this is more just for my personal use.

I use tailscale and self-host an ntfy in a docker container in my homelab. And nothing is exposed to the internet. So beware if you use the ntfy.sh or make your printer publicly available. I'm not your keeper so do what you want.

* Great for notifying you of a pause for a Hueforge filament change!
* Yay! Your print is done and the bed has cooled off!
* Add default messages into your start and end GCODE
* If you heat soak your machine let you know when it's up to temp.
* I'm sure there's many more ways this can be useful.

This just adds one GCODE command to your klipper installation. It sends a http post message to the ntfy server.

## Instalation

I"m still working on the install script and it hasn't been tested. So you can follow the following for a manual installation.

### Manual Installation

1. SSH into the Pi or computer/device that is running Klipper

I use Windows Terminal on Windows, or just a terminal in Linux or MacOS. But putty is another go to for Windows users.

2. Clone this repository & navigate into the repositiory

```
git clone https://github.com/djfroese/klippy_ntfy
cd ~/klippy_ntfy
```
3. Stop Klipper Service
```
sudo service klipper stop
```
4. Create a symlink to to the ntfy.py file in the ~/klipper/klippy/extras folder.
```
ln -s ~/klippy_ntfy/ntfy.py ~/klipper/klippy/extras/ntfy.py
```
5. Start the klipper service
```
 sudo service klipper start
```
6. Finally setup the [ntfy] section in your printer.cfg file

That's it the new GCode Command should be available. Here's how you can use it.

Here's an example:

```
[ntfy] 
ntfyHost: ntfy.sh
ntfyTopic: My_Favourit_3D_Printer
```
> Make sure you subscribe to the same topic on another device in a browser to receive the notification. 

### Usage

In a macro or directly from the console you can now use thet **SEND_NTFY** gcode command.

Test it out from the console to make sure it's working you can just invoke the gcode command

```
SEND_NTFY
```

You should receive a notification almost immediately.

Now for the fun bits! Sending one generic message isn't fun. So you can use these properties to customize the notification.

Here's an example using all the different parameters. For example if you need to do a manual filament change for a Hueforge print.

```
SEND_NTFY TITLE="Print Paused!" BODY="Time to change the colour from yellow to blue" PRIORITY=5 TAGS="yellow_circle,recycle,blue_circle"
```


**TITLE** is the title of the message

**BODY** is the main body of the message for any additional details

**TAGS** you can add any tags. See the ntfy tag short names for all the options

**PRIORITY** lets you set the priority from 1 to 5. See ntfy docs
