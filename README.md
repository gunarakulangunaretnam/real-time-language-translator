# Real Time Voice Recognition based Language Translation Bot

## Introduction

 A voice recognition based tool for translating languages in real time. This tool could be used to translate languages with voice data. For an example, it can listen and, translate that voice data into the target language then, it speaks out as a voice output, similar to a human translator, who listens and then translate in a targeted language.  

 This is not efficient like human translator, it is using the google translate platform as backbone to perform the translation process.


![diagram](github-readme-contents/system-architeture.png)

 ## Technologies & Frameworks

 - Python 3.8
 - GTTS Module
 - SpeechRecognition Module
 - Playsound Module
 - Googletrans Module


### Why GTTS Module?

gTTS (Google Text-to-Speech)is a Python library and CLI tool to interface with Google Translate text-to-speech API. We will import the gTTS library from the gtts module which can be used for speech translation.

**Note:** This module helps to convert text as voice output.


### Why SpeechRecognition Module?

This module gives the ability to perform speech recognition, basically, it could be used to convert speech to text operations.

### Why Playsound Module?

playsound is a “pure Python, cross platform, single function module with no dependencies for playing sounds.” With this module, you can play a sound file with a single line of code:

``` python
from playsound import playsound
playsound('myfile.wav')
```

### Why Googletrans Module?

Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate.

This is core library of this project, which does the translations among languages.

## Execution & Running

**Note:** To perform translation, navigate to the preferred folder, and execute the run.py script to start the program.

```
python run.py

```

Social Media Links
---

* [Linkedin Profile](https://www.linkedin.com/in/gunarakulangunaretnam/)
* [Facebook Page](https://www.facebook.com/gunarakulangunaretnam)
* [Twitter Profile](https://twitter.com/gunarakulan)
* [Instagram Profile](https://www.instagram.com/gunarakulangunaretnam/)
* [Youtube Channel](https://www.youtube.com/channel/UCMWkED5sabgVZSCKjZuRJXA)
