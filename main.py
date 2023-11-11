import requests
from flask import Flask , render_template ,request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def da1():
    return render_template('itog.html')


@app.route('/result',methods=['GET','POST'])
def da2():
    da= request.form['city'].lower()
    itogi = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={da}&appid=adbb2821feabdbc9583b52bec964c8c1').json()
    try:
        city = translator.translate(itogi['name'], dest="ru")
        weather = translator.translate(itogi['weather'][0]['description'], dest="ru")
        temperature = round(float(itogi['main']['temp'] - 273.0 ),2)
        return render_template('daa.html',json_da=city.text , weather=weather.text[0]+weather.text[1:], tempe=temperature)
    except:
        return 'NOT VALID'

if __name__ == '__main__':
    app.run(debug=True)