import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pins = (16, 20, 21)  # (12, 25, 24)  # (16, 20, 21)
a = (100, 10, 50)
f = (.03, .07, 0.14)
pwms = []

for i, p in enumerate(pins):
	GPIO.setup(p, GPIO.OUT)
	pwm = GPIO.PWM(p, f[i])
	pwm.start(a[i])
	pwms.append(pwm)

while True:
	s = raw_input('Hello Ruby!')
	if s == 'q':
		break

GPIO.cleanup()

