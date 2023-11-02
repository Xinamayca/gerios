from flask import Flask
from flask import render_template
import random


def generate_random_temperature():
    """
    Generate a random floating-point number between 20 and 40 .
    """
    temperature = random.uniform(15, 40)
    temperature = round(temperature, 1)
   
    # return  str(temperature) + " C."
    return str(temperature) + " °C "

def generate_random_humidity():
    """
    Generate a random floating-point number between 20 and 100 .
    """
    humidity = random.uniform(0, 100)
    humidity = round(humidity, 1)
   
    # return  str(humidity) +
    return str(humidity) + " %"


def generate_random_light_level():
    """
    Generate a random floating-point number between 0 and 1000 W/m².
    """
    light = random.uniform(0, 1000)
    light = round(light, 4)
   
    # return  str(light) + " W/m²."
    return str(light) + " W/m²"

ListData = \
    [
        (generate_random_temperature(), generate_random_humidity(), generate_random_light_level())
    ]



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',
                           temperature = generate_random_temperature(), 
                           humidity = generate_random_humidity(), 
                           light = generate_random_light_level())


def generate_data():
    ListData.insert(0, (generate_random_temperature(), generate_random_humidity(), generate_random_light_level()))
    if len(ListData) > 15:
        ListData.pop(-1)


@app.route('/measurements')
def measurements():
    generate_data()
    return render_template('measurements.html',
                           measurements = ListData
                           )


if __name__ == '__main__':
    app.run(debug=True, port=8080)



