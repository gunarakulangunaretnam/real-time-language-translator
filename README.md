# Python Real Time Language Translation Bot

This repository contains some python scripts which can translate languages with audio processing. These scripts are written in python with some modules.

###### How does it work

1. Convert audio speeches into texts with [speech-recognition library](https://pypi.org/project/SpeechRecognition/).
2. Translate the text into another language with [googletrans library](https://pypi.org/project/googletrans/)
3. Convert the translated text into voice [gtts library](https://pypi.org/project/gTTS/)
4. Play the voice as sound [playsound library](https://pypi.org/project/playsound/)

###### System Architecture

![System Architecture](/system-architeture.png)
