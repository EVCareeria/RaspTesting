from sense_hat import SenseHat
import time
import urllib.request

sense = SenseHat()
deviceid=10

while True:
    type=1
    temp = sense.get_temperature()*0.75 -7
    print("Temp: %s C" % temp)
    url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(temp)+"&type="+str(type)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print(htmltext)
    sense.set_rotation(180)
    sense.show_message("%.1f C" % temp, scroll_speed=0.12, text_colour=[255, 255, 255])
    time.sleep(4)

    type=2
    humidity = sense.get_humidity()
    print("humidity: %s C" % humidity)
    url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(humidity)+"&type="+str(type)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print(htmltext)
    sense.set_rotation(180)
    sense.show_message("%.1f C" % humidity, scroll_speed=0.12, text_colour=[255, 255, 255])
    time.sleep(4)

    type=3
    pressure = sense.get_pressure()
    print("pressure: %s C" % pressure)
    url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(pressure)+"&type="+str(type)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print(htmltext)
    sense.set_rotation(180)
    sense.show_message("%.1f C" % pressure, scroll_speed=0.12, text_colour=[255, 255, 255])
    time.sleep(4)

    type=4
    heading = sense.get_compass()
    if heading < 45 or heading > 315:
        suunta = 'N'
    elif heading < 135:
        suunta = 'E'
    elif heading < 225:
        suunta = 'S'
    else:
        suunta = 'W'
        
    print("heading: %s C" % heading)
    url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(heading)+"&type="+str(type)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print(htmltext)
    sense.set_rotation(180)
    sense.show_message("%.1f C" % heading, scroll_speed=0.12, text_colour=[255, 255, 255])
    time.sleep(4)


