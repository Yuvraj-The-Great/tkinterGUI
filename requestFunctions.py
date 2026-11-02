#raspberry pi url
pi_url = "127.0.0.1"
import requests

#forward when the up button is pressed
def up():
    try:
        #Sends a JSON message to Raspi to Forward
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "forward"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"

    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"
    
#backward when the down button is clicked
def down():
    try:
        #Sends a JSON message to Raspi to Backward
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "backward"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:    
        print("Failed")
        return "Failed"

#right when the right button is clicked
def right():
    try:
        #Sends a JSON message to Raspi to Right
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "right"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"
    
#left when the left button is clicked
def left():
    try:
        #Sends a JSON message to Raspi to Left
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "left"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"
        
#play when the play button is clicked
def play():
    try:
        #Sends a JSON message to Raspi to Play
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "play"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"

    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"

#stop when the stop button is clicked
def stop():
    try:
        #Sends a JSON message to Raspi to Stop
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "stop"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"
