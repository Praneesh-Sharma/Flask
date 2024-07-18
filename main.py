#Integerate HTML with Flask

#Jinja2 Template engine
'''
{%...%} statements/conditions
{{   }} to print output
{#...#} internal comments
'''

from flask import Flask, redirect, url_for, render_template, request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp = {'score':score, 'res':res}
    return render_template('results.html', result=exp)

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

#Result Checker HTML Page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        sci=float(request.form['science'])
        mat=float(request.form['maths'])
        eng=float(request.form['english'])
        total_score=(sci+mat+eng)/3
    return redirect(url_for('success',score=total_score))

if __name__=='__main__':
    app.run(debug=True)