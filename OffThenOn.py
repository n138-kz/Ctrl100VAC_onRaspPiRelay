import sys
from sys import exit
from time import sleep
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError as e:
    print('[Error] Require module, But not be installed.', file=sys.stderr)
    print(e, file=sys.stderr)
    exit(254)
except Exception as e:
    raise
    exit(255)

RELAY_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

GPIO.output(RELAY_PIN, False)
sleep(0.35)
GPIO.output(RELAY_PIN, True)
sleep(0.35)

exit(0)
