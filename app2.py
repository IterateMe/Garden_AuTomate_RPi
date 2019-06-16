import time

from flask import Flask, g, render_template, flash, redirect, url_for
import RPi.GPIO as GPIO
import API

water_valve = API.EValve(16,15,12)
on_led = API.Led(13)
off_button = API.Button(11, 13)

off_button.set_detection(off_button.close_RPi)

on_led.on()

app = Flask(__name__)

@app.route('/')
def main():
    print(GPIO.input(13))
    return GPIO.input(13)

while True:
    rep = input("[q] to quit")
    if rep == "q":
        GPIO.cleanup()
        KeyboardInterrupt