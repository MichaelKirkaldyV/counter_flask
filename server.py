from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'b166erspoifhodhiei1112895'

@app.route('/')
def index():
	#.get() method returns the value of the key. Sessions are dictionary objects.
	if session.get('count') == 0:
		session['count'] = 1
	return render_template('index.html')

@app.route('/count_two', methods=['POST'])
def add_two():
	session['count'] += 2
	return redirect('/')

@app.route('/plus_one', methods=['POST'])
def plus_one():
	session['count'] += 1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['count'] = 0
	return redirect('/')

app.run(debug=True)