from adafruit_servokit import ServoKit

def move_servo(servo_num, angle):
    kit = ServoKit(channels=16)

    kit.servo[servo_num].angle = angle