from flask import Flask , render_template ,request
from weather import weather_city

app = Flask(__name__)

@app.route('/')
def da1():
    return render_template('itog.html')


@app.route('/result',methods=['GET','POST'])
def da2():
    da = request.form['city'].lower()
    if weather_city(da):
        city , weather , temperature = weather_city(da)
        return render_template('daa.html',json_da=city, weather=weather , tempe=temperature)
    else:
        return 'NOT VALID'

if __name__ == '__main__':
    app.run(debug=True)
