import tello

video=True

drone = tello.Tello('', 8889, video=video)
print("battery:",drone.get_battery(),"%")
#drone.takeoff()

"""ここから"""
import time
time.sleep(100)
"""ここまで"""

#drone.land()
drone.close()