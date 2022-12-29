#Dependencies
Resemble.ai - This app we utilize the API to generate a skeleton voice. This is used for potatoSay and tools/generateVoice.py

## Architecture
![Architecture](architecture/potaot.png)

## KNOWN BUGS
- PotatoSay.sh can't be executed remotely

## LOST
Some of the system commands to prep the raspberry pi are not recorded, but generally:
- Starting Pigpoid at boot
- Ensuring Legacy Camera Support in raspi-config
- Ensuring USB Audio in raspi-config
- Installing Python / System Libs
- Creating and placing AWS CREDS
