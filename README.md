![REHABPAINANALYSER](https://raw.githubusercontent.com/joab40/RehabPainAnalyzer/data/logo.jpg)
# RehabRawAnalyser
Pain Analyzer App

### How it works
Collect everyday stats

## Installation
Unfortunately there is no boundle installation scripts or apk available. (WORKING ON IT)

```sh
git clone http://github.com/joab40/Alpha
```

#### Rasberry Pi Setup:
Pyaudio Minimum req. version 2.9

```sh
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
cd pyaudio;sudo python /setup.py install
```
```sh
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev python-dev 
sudo apt-get install python-pygame
sudo apt-get install flac
sudo apt-get espeak 
```
```sh
pip install aiml
pip install SpeechRecognition
pip install pyvona
pip install pyyaml
pip install yandex
```
## Running (Run)
#### Basic
```sh
./alpha.py
```
#### TextMode
```sh
./alpha.py -t (textmode without stt or tts)
```
#### Option
```sh
./alpha --debug
```


## Supported "verified" Hardware
 - Samsung Galaxy S5

## Supported "verified" Software
 - Andriod 5.0
 - Linux Ubuntu 16.04

## Inspired by
Train and recovery

###  Training Comunity
```sh
https://rawfitness.se

```
