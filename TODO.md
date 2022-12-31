#TODO

## IN PROGRESS
- Mouth more precise
- change how scare delay time works - let commands interrupt

- Create an APP that allows for control of potato (likely Running on RaspPi)
  - Scheduled Sayings
  - Say on demand (show resemble usage)
  - Turn on / off - mostly for LED / POWER
  - Change Mode
  - Manageclips
  - Add metadata to clips
  - local access from 10.22 network static front end to python API raspberrypi.local/api/

- Move to Pub/Sub


##Tech Debt
- Move S3 / API calls to SNS - Potato on Pub / Sub
- Figure out how to have pub sub interrupt pauses in loop (or write a function to handle this)
- break code out into classes / clean up / lib
- Talking Exponential Backoff

##Product / Features
- Scheduled hours for motion detection
- Break Pause Actions
- Eye Movement
- Body Movement
- Eyebrow Movement
- Add arbitrary API key to lock down AWS API
- Add Facial recognition
- Add AI Responses - with limit on api calls (make sure resemble bill cheap)
- Pause On / Off
