import tello, time

video=True

drone = tello.Tello('', 8889, video=video)
print("battery:",drone.get_battery(),"%")
drone.takeoff()

"""ここから"""
time.sleep(10)
"""ここまで"""

drone.land()
drone.close()