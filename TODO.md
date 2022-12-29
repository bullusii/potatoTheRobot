#TODO

## IN PROGRESS
Rebranding to Potato
Moving code to functions / libraries utilizing globals
Total mess of config / layered loads to reuse code

##Tech Debt
- Move S3 / API calls to SNS - Potato on Pub / Sub
- Figure out how to have pub sub interrupt pauses in loop (or write a function to handle this)
- break code out into classes / clean up / lib
- Talking Exponential Backoff
- Add script to add some commands to System global /usr/local/bin - symlinks
- send to git as app and api separate

##Product / Features
- Scheduled hours for motion detection
- Break Pause Actions
- Eye Movement
- Body Movement
- Eyebrow Movement
- Add arbitrary API key to lock down AWS API
- Add Facial recognition
- Add AI Responses - with limit on api calls (make sure resemble bill cheap)
- Create an APP that allows for control of potato (likely Running on RaspPi)
  - Scheduled Sayings
  - Say on demand
  - Turn on / off - mostly for LED / POWER
  - Change Mode
  - Pause On / Off
