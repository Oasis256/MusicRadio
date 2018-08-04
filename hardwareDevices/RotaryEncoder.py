import RPi.GPIO as GPIO
from threading import Thread


class RotaryEncoder:
    # Reads the rotary encoder.  Used to read adjustments/turns to switch between frequencies, and
    #   button presses to switch to next band.

    def __init__(self, gpioEncoderPin1, gpioEncoderPin2, gpioPressPin, encoderKnobRotated, encoderButtonPressed):
        self.knobCallback = encoderKnobRotated
        self.buttonCallback = encoderButtonPressed

        self.rotaryCounter = 0
        self.newCounter = 0
        self.currentA = 1
        self.currentB = 1
        self.lockRotary = threading.Lock()

        self.gpioEncoderPin1 = gpioEncoderPin1
        self.gpioEncoderPin2 = gpioEncoderPin2

        # initialize interrupt handler
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)  # Use BCM mode

        # define the Encoder switch inputs
        GPIO.setup(self.gpioEncoderPin1, GPIO.IN)
        GPIO.setup(self.gpioEncoderPin2, GPIO.IN)
        GPIO.setup(self.gpioPressPin,    GPIO.IN)

        # setup callback thread for the A and B encoder
        # use interrupts for all inputs
        GPIO.add_event_detect(gpioEncoderPin1, GPIO.RISING, callback=rotary_interrupt)  # NO bouncetime
        GPIO.add_event_detect(gpioEncoderPin2, GPIO.RISING, callback=rotary_interrupt)  # NO bouncetime
        GPIO.add_event_detect(gpioPressPin,    GPIO.RISING, callback=self.buttonCallback)

    def tick(self):
        # Typically called at 100 Hz
        # because of threading - make sure no thread changes value until we get them and reset them

        self.lockRotary.acquire()
        self.newCounter = self.rotaryCounter  # get counter value
        self.rotaryCounter = 0
        self.lockRotary.release()

        if self.newCounter != 0:
            self.knobCallback(self.newCounter*abs(self.newCounter))

    def rotary_interrupt(self, A_or_B):
        # Rotary encoder interrupt - this one is called for both inputs from rotary switch (A and B)
        # read both of the switches
        Switch_A = GPIO.input(self.gpioEncoderPin1)
        Switch_B = GPIO.input(self.gpioEncoderPin2)

        # Now check if state of A or B has changed.  If not that means that bouncing caused it
        if self.currentA == Switch_A and self.currentB == Switch_B:  # Same interrupt as before (Bouncing)?
            return  # ignore interrupt!

        self.currentA = Switch_A  # remember new state
        self.currentB = Switch_B  # for next bouncing check

        if (Switch_A and Switch_B):  # Both one active? Yes -> end of sequence
            self.lockRotary.acquire()
            if A_or_B == self.gpioEncoderPin1:  # Turning direction depends on which input gave last interrupt
                self.rotaryCounter += 1
            else:  # So depending on direction either increase or decrease counter
                self.rotaryCounter -= 1
            self.lockRotary.release()
        return
