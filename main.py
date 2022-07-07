from pyowm import OWM

owm = OWM('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')    #Enter your openweathermap API here
mgr = owm.weather_manager()

observation = mgr.weather_at_place('xxxxxxxx, xx')   #Enter your city name, country code  according to openweathermap website
w = observation.weather


while True:
    print("Menu:\n\n1.Detailed status\n2.Wind\n3.humidity\n4.temperature\n5.rain\n6.heat index\n7.clouds\n8.Quit")
    opt=int(input('Enter your choice : '))
    print("----------------------------------------------------\n")

    if opt==1:
        print("Detailed status --> ",w.detailed_status)
    elif opt==2:
        print("Wind --> ",w.wind())
    elif opt==3:
        print("Humidity --> ",w.humidity)
    elif opt==4:
        print("Temperature --> ",w.temperature('celsius'))
    elif opt==5:
        print("Rain --> ",w.rain)
    elif opt==6:
        print("Heat Index --> ",w.heat_index)
    elif opt==7:
        print("Clouds --> ",w.clouds)
    elif opt==8:
        break
    else:
        print("Enter valid input")
    
    print("\n----------------------------------------------------\n")
