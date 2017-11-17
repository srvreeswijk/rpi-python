from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 5
SEND_PIN = 27

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SEND_PIN, GPIO.OUT)
    beginning_time = datetime.now()
    print '**Start sending**'
    n=0
    while true:
        GPIO.output(RECEIVE_PIN, n))
        n=n+1
    GPIO.cleanup()

    print '**Processing results**'
    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds + RECEIVED_SIGNAL[0][i].microseconds/1000000.0
    print   RECEIVED_SIGNAL
    #print '**Plotting results**'
    #pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
    #pyplot.axis([0, MAX_DURATION, -1, 2])
    #pyplot.show()

