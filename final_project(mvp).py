from gpiozero import MotionSensor, LED
import time
import subprocess
from pathlib import Path

audio_file = Path(__file__).parent / "intruder.mp3"


# Initialize PIR sensor on GPIO 17
pir = MotionSensor(17)
led = LED(18)


print("PIR program started!")
print("Monitoring GPIO 17...")
seconds = 0

audio_process = None



while True:
    if pir.value:
        #print("Motion detected!")
        seconds += 1
    
    
    else:
        led.off()
        seconds= 0

        if audio_process is not None: #this is True either when a) audiio is still playing, b) audio stopped but audio_process is still not None
            if audio_process.poll() is None:  # Checks for a)— .poll() returns None when audio is still playing
                audio_process.terminate() # .terminate() stops audio
                audio_process.wait() #program doesn't advance until .terminate() is fully executed

            audio_process = None  # Reset the audio process variable  
    
    print("Sensor output:", pir.value)
    time.sleep(1)
    
    
    
    if seconds >= 2:
        if audio_process is None:
            led.on()
            audio_process = subprocess.Popen(["mpg123", "-q", str(audio_file)])
