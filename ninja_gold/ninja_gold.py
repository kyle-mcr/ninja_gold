from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'root'

@app.route('/')         
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template("ninja_gold.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    print("Got Post Info")
    print(request.form)
    if request.form['place'] == 'farm':
        session['gold'] += int(10)
    elif request.form['place'] == 'cave':
        session['gold'] += int(10)
    elif request.form['place'] == 'house':
        session['gold'] += int(10)
    elif request.form['place'] == 'casino':
        session['gold'] += int(10)
    return redirect("/") 

@app.route('/reset')         
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True)
