# Copied from https://github.com/IrvKalb/pyghelpers/blob/master/pyghelpers/pyghelpers.py
# Homework was just Copy-Pasting these code.
# Licensed with BSD-2-Clause License

import time


#  Timer
class Timer():
    """
    This class is used to create a very simple Timer.

    Typical use:

    1)  Create a Timer object:

        myTimer = pyghelpers.Timer(10)

    2)  When you want the timer to start running, make this call:

        myTimer.start()

        You can also call this method to restart the timer after it finishes.

    3)  In your big loop, check to see if the timer has finished:

        finished = myTimer.update()

        Normally returns False, but returns True when the timer is finished

    Parameters:
        | timeInSeconds - the duration of the timer, in seconds (integer or float)

    Optional keyword parameters:
        | nickname - an internal name to associate with this timer (defaults to None)
        | callback - a function or object.method to be called back when the timer is finished
        |            The nickname of the timer will be passed in if a callback is made (defaults to None)

    """

    def __init__(self, timeInSeconds, nickname=None, callBack=None):
        self.timeInSeconds = timeInSeconds
        self.nickname = nickname
        self.callBack = callBack
        self.savedSecondsElapsed = 0.0
        self.running = False
        self.paused = False
        self.pauseCounter = 0  # counts how many calls to pause without a resume

    def start(self, newTimeInSeconds=None):
        """Start the timer running (starts at zero).
        Allows you to optionally specify a different amount of time.

        Optional keyword parameter:
        | newTimeInSeconds - a new duration for the timer (integer or float, default None)

        """
        if newTimeInSeconds is not None:
            self.timeInSeconds = newTimeInSeconds
        self.running = True
        self.startTime = time.time()
        self.paused = False
        self.timePaused = None
        self.pauseCounter = 0

    def update(self):
        """Call this in every frame to update the timer

        Returns:
           |   False - most of the time
           |   True - when the timer is finished
           |          (you can use this indication, or set up a callback)

        """
        if not self.running:
            return False
        self.savedSecondsElapsed = time.time() - self.startTime
        if self.savedSecondsElapsed < self.timeInSeconds:
            return False  # running but hasn't reached limit

        else:  # timer has finished
            self.running = False
            if self.callBack is not None:
                self.callBack(self.nickname)

            return True  # True here means that the timer has ended

    def getTime(self):
        """ Call this if you want to know how much has elapsed

        Returns:
           |   0 - if the Timer is not running
           |   seconds elapsed since start, as a float

        """
        if self.running or self.paused:
            self.savedSecondsElapsed = time.time() - self.startTime

        return self.savedSecondsElapsed

    def pause(self):
        """Pauses the timer"""
        self.pauseCounter = self.pauseCounter + 1
        self.timePaused = time.time()
        self.paused = True

    def resume(self):
        """Resumes the timer after a pause"""
        if self.pauseCounter == 0:
            print('Warning - called resume timer but the timer is not paused ... ignored')
        else:
            self.pauseCounter = self.pauseCounter - 1
        if self.pauseCounter != 0:
            return  # don't resume

        # OK to resume
        pauseTime = time.time() - self.timePaused
        self.secondsStart = self.secondsStart + pauseTime
        self.paused = False

    def stop(self):
        """Stops the timer"""
        self.getTime()  # remembers final self.savedSecondsElapsed
        self.running = False
        self.paused = False
        self.pauseCounter = 0


# CountUpTimer class
class CountUpTimer():
    """
    This class is used to create a Timer that counts up (starting at zero).

    Its intended use is where you want to continuously display the time in a window (using a DisplayText object).

    Typical use:

    1)  Create a CountUpTimer object:

        myTimer = pyghelpers.CountUpTimer()

    2)  When you want the timer to start running, make this call:

        myTimer.start()

        This method can also be called to restart the timer.

    3)  Whenever you want to get the current time (in seconds since start), you can call any of:

        theTime = myTimer.getTime() # gets time as a float

        theTime = myTimer.getTimeInSeconds() # gets the time as an integer number of seconds

        theTime = myTimer.getTimeInHHMMSS() # gets the time in HH:MM:SS string format

        One of the above should be called every time through your main loop.

    4)  If you want to stop the timer, call:

        myTimer.stop()


    Parameters:
        | none

    """

    def __init__(self):
        self.running = False
        self.savedSecondsElapsed = 0.0
        self.secondsStart = 0  # safeguard
        self.paused = False
        self.timePaused = None
        self.pauseCounter = 0  # counts how many calls to pause without a resume

    def start(self):
        """Start the timer running (starts at zero).  Can be called to restart the timer, for example to play a game multiple times"""
        self.secondsStart = time.time()  # get the current seconds and save the value
        self.running = True
        self.paused = False
        self.savedSecondsElapsed = 0.0
        self.pauseCounter = 0

    def getTime(self):
        """Returns the time elapsed as a float"""
        if not self.running or self.paused:
            return self.savedSecondsElapsed  # do nothing

        self.savedSecondsElapsed = time.time() - self.secondsStart
        return self.savedSecondsElapsed  # returns a float

    def getTimeInSeconds(self):
        """Returns the time elapsed as an integer number of seconds"""
        nSeconds = int(self.getTime())
        return nSeconds

    # Updated version using fStrings
    def getTimeInHHMMSS(self, nMillisecondsDigits=0, forceFullHHMMSS=False):
        """Returns the elapsed time as a HH:MM:SS.mmm formatted string

        Parameters:

        Optional keyword parameters:
            | nMillisecondsDigits - number of milliseconds digits to include (defaults to 0)
            |    If specified, returned string will include nMillisecondsDigits of milliseconds digits
            | forceFullHHMMSS forces the output to be in full HH:MM:SS format (defaults to False)

        """
        nSeconds = self.getTime()
        mins, secs = divmod(nSeconds, 60)
        hours, mins = divmod(int(mins), 60)

        if nMillisecondsDigits > 0:
            secondsWidth = nMillisecondsDigits + 3
        else:
            secondsWidth = 2

        if forceFullHHMMSS:
            output = f'{hours:02d}:{mins:02d}:{secs:0{secondsWidth}.{nMillisecondsDigits}f}'
        elif hours > 0:
            output = f'{hours:d}:{mins:02d}:{secs:0{secondsWidth}.{nMillisecondsDigits}f}'
        elif mins > 0:
            output = f'{mins:d}:{secs:0{secondsWidth}.{nMillisecondsDigits}f}'
        else:
            output = f'{secs:.{nMillisecondsDigits}f}'

        return output

    def stop(self):
        """Stops the timer"""
        self.getTime()  # remembers final self.savedSecondsElapsed
        self.running = False
        self.paused = False
        self.pauseCounter = 0

    def pause(self):
        """Pauses the timer"""
        self.pauseCounter = self.pauseCounter + 1
        self.timePaused = time.time()
        self.paused = True

    def resume(self):
        """Resumes the timer after a pause"""
        if self.pauseCounter == 0:
            print('Warning - called resume timer but the timer is not paused ... ignored')
        else:
            self.pauseCounter = self.pauseCounter - 1
        if self.pauseCounter != 0:
            return  # don't resume

        # OK to resume
        pauseTime = time.time() - self.timePaused
        self.secondsStart = self.secondsStart + pauseTime
        self.paused = False


#
# CountDownTimer class
#
class CountDownTimer():
    """
    This class is used to create a Timer that counts down from a given starting number of seconds.
    Its intended use is where you want to continuously display the time in a window (using a DisplayText object).

    Typical use:

    1)  Create a CountDownTimer object:

        myTimer = pyghelpers.CountDownTimer(60)   # start the timer at 60 seconds

    2)  When you want the timer to start running, make this call:

        myTimer.start()

        This method can also be used to restart the timer.

    3)  Whenever you want to get the remaining time (in seconds since start), you can call any of:

        theTime = myTimer.getTime() # gets time as a float

        theTime = myTimer.getTimeInSeconds() # gets the time as an integer number of seconds

        theTime = myTimer.getTimeInHHMMSS() # gets the time in HH:MM:SS string format

    4)  If you want to stop the timer, call:

        myTimer.stop()


    Parameters:
        | nStartingSeconds - the starting point for the timer, in seconds (integer or float)

    Optional keyword parameters:
        | stopAtZero - should the timer stop when it reaches zero (defaults to True)
        | nickname - an internal name used to refer to this timer (defaults to None)
        | callback - a function or object.method to be called back when the timer is finished
        |            The nickname of the timer will be passed in when the callback is made (defaults to None)

    """

    def __init__(self, nStartingSeconds, stopAtZero=True, nickname=None, callBack=None):
        self.nStartingSeconds = nStartingSeconds
        self.stopAtZero = stopAtZero
        self.nickname = nickname
        self.callBack = callBack

        self.running = False
        self.secondsSavedRemaining = 0.0
        self.reachedZero = False
        self.pauseCounter = 0  # counts how many calls to pause without a resume

    def start(self, newStartingSeconds=None):
        """Start the timer running starting at nStartingSeconds (or optional different setting)"""
        secondsNow = time.time()
        if newStartingSeconds is not None:
            self.nStartingSeconds = newStartingSeconds
        self.secondsEnd = secondsNow + self.nStartingSeconds
        self.reachedZero = False
        self.running = True
        self.paused = False
        self.timePaused = None
        self.pauseCounter = 0

    def getTime(self):
        """Returns the remaining time as a float number of seconds"""
        if not self.running or self.paused:
            return self.secondsSavedRemaining

        self.secondsSavedRemaining = self.secondsEnd - time.time()
        if self.stopAtZero and (self.secondsSavedRemaining <= 0):
            self.secondsSavedRemaining = 0.0
            self.running = False
            self.reachedZero = True

        return self.secondsSavedRemaining  # returns a float

    def getTimeInSeconds(self):
        """Returns the remaining time as an integer number of seconds"""
        nSeconds = int(self.getTime())
        return nSeconds

    # Updated version using fStrings
    def getTimeInHHMMSS(self, nMillisecondsDigits=0, forceFullHHMMSS=False):
        """Returns the remaining time as a HH:MM:SS.mmm formatted string

        Parameters:

        Optional keyword parameters:
            | nMillisecondsDigits - number of milliseconds digits to include (defaults to 0)
            |    If specified, returned string will include nMillisecondsDigits of milliseconds digits
            | forceFullHHMMSS forces the output to be in full HH:MM:SS format (defaults to False)

        """
        nSeconds = self.getTime()
        mins, secs = divmod(nSeconds, 60)
        hours, mins = divmod(int(mins), 60)

        if nMillisecondsDigits > 0:
            secondsWidth = nMillisecondsDigits + 3
        else:
            secondsWidth = 2

        if forceFullHHMMSS:
            output = f'{hours:02d}:{mins:02d}:{secs:0{secondsWidth}.{nMillisecondsDigits}f}'
        elif hours > 0:
            output = f'{hours:d}:{mins:02d}:{secs:0{secondsWidth}.{nMillisecondsDigits}f}'
        elif mins > 0:
            output = f'{mins:d}:{secs:0{secondsWidth}.{nMillisecondsDigits}f}'
        else:
            output = f'{secs:.{nMillisecondsDigits}f}'

        self.savedSecondsElapsed = output
        return output

    def stop(self):
        """Stops the timer """
        self.getTime()  # remembers final self.savedSecondsElapsed
        self.running = False
        self.paused = False
        self.pauseCounter = 0

    def ended(self):
        """Call to see if the timer has reached zero. Should be called every time through the loop"""
        dontCare = self.getTime()  # called to  set self.reachedZero
        if self.reachedZero:
            self.reachedZero = False  # reset
            if self.callBack is not None:
                self.callBack(self.nickname)
            return True
        else:
            return False

    def pause(self):
        """Pauses the timer"""
        self.pauseCounter = self.pauseCounter + 1
        self.timePaused = time.time()
        self.paused = True

    def resume(self):
        """Resumes the timer after a pause"""
        if self.pauseCounter == 0:
            print('Warning - called resume timer but the timer is not paused ... ignored')
        else:
            self.pauseCounter = self.pauseCounter - 1
        if self.pauseCounter != 0:
            return  # don't resume

        # OK to resume
        pauseTime = time.time() - self.timePaused
        self.secondsStart = self.secondsStart + pauseTime
        self.paused = False