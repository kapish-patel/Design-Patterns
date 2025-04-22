# main method
from WeatherStation import WeatherStation
from PhoneDisplayObs import PhoneDisplayObs
from WebsiteWidgetObs import WebsiteWidgetObs
from SmartHomeSystemObs import SmartHomeSystemObs


def main():

    weather_station = WeatherStation()
    devices = {
        "PhoneDisplay": [],
        "WebsiteWidget": [],
        "SmartHomeSystem": []
    }

    while True:
        print("1. Add Device", end='\n')
        print("2. Remove Device", end='\n')
        print("3. Update Weather Station", end='\n')
        print("4. Exit", end='\n')
        choice = input("Enter your choice: ")
        if choice == '1':
            print("1. PhoneDisplay", end='\n')
            print("2. WebsiteWidget", end='\n')
            print("3. SmartHomeSystem", end='\n')
            device_choice = input("Enter your choice: ")

            print('\n')
            print('1. Temperature', end='\n')
            print('2. Humidity', end='\n')
            print('3. Pressure', end='\n')
            observing_choice = input("Enter your choices: ")
            observing = []
            for obs in observing_choice:
                if obs == '1':
                    observing.append('Temperature')
                elif obs == '2':
                    observing.append('Humidity')
                elif obs == '3':
                    observing.append('Pressure')
            
            if device_choice == '1':
                devices["PhoneDisplay"].append(PhoneDisplayObs(weather_station, observing))
            elif device_choice == '2':
                devices["WebsiteWidget"].append(WebsiteWidgetObs(weather_station, observing))
            elif device_choice == '3':
                devices["SmartHomeSystem"].append(SmartHomeSystemObs(weather_station, observing))
            print("Device added successfully")
        elif choice == '2':
            print("1. PhoneDisplay", end='\n')
            print("2. WebsiteWidget", end='\n')
            print("3. SmartHomeSystem", end='\n')
            device_choice = input("Enter your choice: ")

            if device_choice == '1':
                devices["PhoneDisplay"].pop()
            elif device_choice == '2':
                devices["WebsiteWidget"].pop()
            elif device_choice == '3':
                devices["SmartHomeSystem"].pop()
            print("Device removed successfully")
        
        elif choice == '3':
            print("1. Set Temperature", end='\n')
            print("2. Set Humidity", end='\n')
            print("3. Set Pressure", end='\n')
            weather_choice = input("Enter your choice: ")
            if weather_choice == '1':
                temperature = int(input("Enter temperature: "))
                weather_station.set_measurements(temperature=temperature)
            elif weather_choice == '2':
                humidity = int(input("Enter humidity: "))
                weather_station.set_measurements(humidity=humidity)
            elif weather_choice == '3':
                pressure = int(input("Enter pressure: "))
                weather_station.set_measurements(pressure=pressure)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")
            break

if __name__ == '__main__':
    main()