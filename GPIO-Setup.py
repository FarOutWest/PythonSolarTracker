#!/usr/bin/env python


import os

os.system("gpio -g pwm 18 0")
os.system("gpio -g mode 18 pwm")
os.system("gpio -g mode 12 pwm")
os.system("gpio pwmr 2000")
os.system("gpio pwm-ms")
