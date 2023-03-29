import sched
import os
import time
from src.bpm import getBpm

s = sched.scheduler(time.time, time.sleep)
def main(sc): 
    getBpm()
    sc.enter(10, 1, main, (sc,))

s.enter(0, 1, main, (s,))

s.run()
