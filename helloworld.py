from flask import *
import smtplib
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		message = request.form['textbox']
		exe(message)
		return render_template('index.html')
	else:
		return render_template('index.html')

def getSMTP():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	try:
		server.login('myomessenger@gmail.com', 'hacktcnj2015')
	except smtplib.SMTPAuthenticationError:
		print 'Invalid GMail Information Provided...'
		sys.exit()
	return server;

def exe(message):
	server = getSMTP()
	server.sendmail('New message!', '********', message);

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)