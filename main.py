import time
import random

def get_distance():
    # Simulate GPS-based distance measurement
    return random.uniform(0, 2)  # Distance in km (0 to 2km for simulation)

class TrafficSignal:
    def __init__(self, location):
        self.location = location  # ✅ Fixed syntax error
        self.state = "RED"
    
    def change_signal(self, state):
        self.state = state
        print(f"Traffic Signal at {self.location} changed to {self.state}")
    
    def emergency_override(self):
        print(f"Ambulance detected within 1km! Prioritizing emergency vehicle at {self.location}")
        self.block_other_lanes()
        self.change_signal("GREEN")
        time.sleep(5)  # Keep green for ambulance passage
        self.change_signal("RED")
    
    def block_other_lanes(self):
        print(f"Blocking other lanes at {self.location} to clear path for ambulance")

def detect_ambulance():
    distance = get_distance()
    print(f"Ambulance distance: {distance:.2f} km")
    return distance <= 1.0  # Detect if ambulance is within 1km

if __name__ == "__main__":
    signal = TrafficSignal("Main Street")
    while True:
        if detect_ambulance():
            signal.emergency_override()
        else:
            signal.change_signal("RED")  # Default signal state
        time.sleep(10)  # Wait before next check
