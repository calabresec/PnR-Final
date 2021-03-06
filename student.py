import pigo
import time
import random

'''
MR. A's Final Project Student Helper
'''


class GoPiggy(pigo.Pigo):
    ########################
    ### CONTSTRUCTOR - this special method auto-runs when we instantiate a class
    #### (your constructor lasted about 9 months)
    ########################

    def __init__(self):
        print("Your piggy has be instantiated!")
        # Our servo turns the sensor. What angle of the servo( ) method sets it straight?
        self.MIDPOINT = 85
        # YOU DECIDE: How close can an object get (cm) before we have to stop?
        self.STOP_DIST = 30
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.LEFT_SPEED = 115
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.RIGHT_SPEED = 155
        # This one isn't capitalized because it changes during runtime, the others don't
        self.turn_track = 0
        # Our scan list! The index will be the degree and it will store distance
        self.scan = [None] * 180
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.menu()

    ########################
    ### CLASS METHODS - these are the actions that your object can run
    #### (they can take parameters can return stuff to you, too)
    #### (they all take self as a param because they're not static methods)
    ########################


    ##### DISPLAY THE MENU, CALL METHODS BASED ON RESPONSE
    def menu(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like to add an experimental method
        menu = {"n": ("Navigate forward", self.nav),
                "d": ("Dance", self.dance),
                "c": ("Calibrate", self.calibrate),
                "w": ("Sweep", self.sweep),
                "o": ("Count Obstacles", self.count_obstacles),
                "t": ("Total Obstacles", self.count_obstacles),
                "s": ("Check status", self.status),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = raw_input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    def sweep(self):
        for x in range(20, 160, 2):
            self.servo(x)
            if self.dist() < 30:
                print('AAHHH')
                break

    def count_obstacles(self):
        # run scan
        self.wide_scan()
        # count how many obstacles I found
        counter = 0
        # starting state assumes no obstacle
        found_something = False
        # loop through all of my scan data
        for x in self.scan:
            # if x is not none and really close
            if x and x < self.STOP_DIST:
                # if I've already found something
                if found_something:
                    print("obstacle continues")
                    # if this is a new obstacle
                else:
                    # switch my tracker
                    found_something = True
                    print("start of new obstacle")
                    # if my data shows safe distances
            if x and x > self.STOP_DIST:
                # if my tracker had been triggered...
                if found_something:
                    print("end of obstacle")
                    # reset tracker
                    found_something = False
                    # increase count of obstacles
                    counter += 1
        print(' Total number of obstacles in this scan:' + str(counter))
        return counter

    #


    def turn_test(self):
        while True:
            ans = raw_input('Turn right, left or stop? (r/l/s): ')
            if ans == 'r':
                val = int(raw_input('/nBy how much?: '))
                self.encR(val)
            elif ans == 'l':
                val = int(raw_input('/nBy how much?: '))
                self.encL(val)
            else:
                break
        self.restore_heading()

    def sweep(self):
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, 2):
            self.servo(x)
            self.scan[x] = self.dist()
        print("Here's what I saw")
        print(self.scan)

    def safety_dance(self):
        for y in range(3):
            for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, 2):
                self.servo(x)
                if self.dist() > 30:
                    print("Lets dance!")
                if self.dist() < 30:
                    print("Abort mission")
                    return
                self.encR(7)
            self.dance()

            ## def total_obstacles(self):
            # counter = 0
            # for x in range(4):
            # counter += self.count_obstacles
            #  self.encR(6)
            # print('Total number of obstacles in the scan' + str(counter))
            # turn your robot

    def restore_heading(self):
        print("Now I'll turn back to the starting postion.")
        # make self.turn_track go back to zero
        if self.turn_track > 0:
            print('I must have turned right a lot now I should turn left')
            self.encL(abs(self.turn_track))
        elif self.turn_track < 0:
            print('I must have turned left a lot and now I have to self.encR(??)')
            self.encR(abs(self.turn_track))
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def encR(self, enc):
        pigo.Pigo.encR(self, enc)
        self.turn_track += enc

    def encL(self, enc):
        pigo.Pigo.encL(self, enc)
        self.turn_track -= enc

    # YOU DECIDE: How does your GoPiggy dance?



    # YOU DECIDE: How does your GoPiggy dance?
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        self.shimmy()
        self.twirl()
        self.back_it_up()
        self.chacha()
        self.head_shake()

    def head_shake(self):
        for x in range(2):
            self.servo(30)
            self.servo(150)
            self.servo(self.MIDPOINT)

    def shimmy(self):
        print('shimmy')
        for x in range(3):
            self.encR(3)
            self.servo(140)
            self.encL(3)

    def twirl(self):
        print('twirl')
        for x in range(2):
            self.encB(15)
            self.encR(30)
            self.encL(15)
            self.encR(30)
            self.encF(15)
            self.stop()

    def back_it_up(self):
        print('back_it_up')
        for x in range(3):
            self.encB(30)
            self.encL(30)
            self.encB(30)
            self.encR(30)
            self.encB(30)
            self.encR(30)
            self.encF(30)
            self.stop()

    def chacha(self):
        print('chacha')
        for x in range(2):
            self.encR(15)
            self.encL(30)
            self.encB(20)
            self.encR(15)
            self.encL(30)
            self.encB(20)

    def head_shake(self):
        for x in range(2):
            self.servo(30)
            self.servo(150)
        self.servo(self.MIDPOINT)

    ########################
    ### MAIN LOGIC LOOP - the core algorithm of my navigation
    ### (kind of a big deal)
    ########################

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("[ Press CTRL + C to stop me, then run stop.py ]\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        # this is the loop part of the "main logic loop"

        # count = 0
        while True:
            if self.is_clear():
                self.fwd()
            else:
                self.stop()
            while True:
                self.check_left()
            if self.dist() < self.STOP_DIST *1.5:
                self.check_right()


                #self.servo(self.MIDPOINT)
                #encF 75% of the distance scanned (testing)
                #self.encF(int(self.dist()*.65))
                #count += 1

            # trying to make robot move backwards when locating obstacle
            #if self.dist() < 15:
                #self.encB(2)

            #moves back toward initial direction after moving backwards
            #if count > 3 and self.turn_track != 0:
                #self.restore_heading()
                #count = 0
            #answer = self.choose_path()
            #if answer == "left":
                #self.encL(3)
            #elif answer == "right":
                #self.encR(3)

                # trying to change navigation
                # trying to make the robot move further when clear
                #debating whether to put turn track in

    # how do I get it to loop in and switch between left and right checks
    # should I make it a chain
    def check_right(self):
        self.servo(self.MIDPOINT+15)
        if self.dist() < self.STOP_DIST *1.5:
            if self.dist() < 5:
                self.stop()
                self.encB(2)
            self.set_speed(self.LEFT_SPEED, int(self.RIGHT_SPEED * .4))
            return false
        elif self.dist() < self.STOP_DIST:
                time.sleep(.01)
            self.set_speed(self.LEFT_SPEED, int(self.RIGHT_SPEED * .2))
                # check if something is close
        elif self.dist() < self.STOP_DIST * 3:
                # SOFTER TURN
        self.set_speed(self.LEFT_SPEED, int(self.RIGHT_SPEED * .5))
    # restore default speeds now that we're successful
    self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)
    return True  # we look cool for now, roll on






    # pulsing forward each time the robot does not see an obstacle
    #def pulse(self, count):
        #while self.is_clear():
           # print("All clear! Pulsing forward")
            #if abs(self.turn_track) > 10:
                #self.encF(15)
           # else:
                #self.encF(30)
           #count += 1

            #if count > 3 and self.turn_track != 0:
               # self.restore_heading()
            #count = 0
            #return count


####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


##################################################################
######## The app starts right here when we instantiate our GoPiggy

try:
    g = GoPiggy()
except (KeyboardInterrupt, SystemExit):
    from gopigo import *

    stop()
