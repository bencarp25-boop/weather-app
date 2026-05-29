import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m&models=ukmo_seamless"

response = requests.get(url)

data = response.json()

temperatures = data["hourly"]["temperature_2m"]
times = data['hourly']['time']

max_hours = len(temperatures)

try:
    hours = int(input('How many hours would you like to show?\n'))

    if hours > max_hours:
        print('You requested too many hours.')
    elif hours <= 0:
        print('Please enter a number greater than 0.')
    else:
    
        for i in range(hours):

            formatted_time = times[i][11:16]

            print(formatted_time)
            print(f'{temperatures[i]} Degrees\n')

except:
    print('Please enter a valid number.')
















