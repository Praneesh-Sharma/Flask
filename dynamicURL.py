#Using dynamic URLs
from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/<int:number>')
def number(number):
    return "The number is " + str(number)

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed with a score of " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed with a score of " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    results=""
    if(marks>30):
        results = "success"
    else:
        results = "fail"
    return redirect(url_for(results,score=marks))


if __name__=='__main__':
    app.run(debug=True)