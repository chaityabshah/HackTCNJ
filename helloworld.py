from flask import *
import smtplib
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		message = request.form['textbox']
		phone = request.form['phnum']
		carrier = request.form['carrier']
		exe(message, phone, carrier)
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
codes = {'.-': 'A',     '-...': 'B',   '-.-.': 'C', 
        '-..': 'D',    '.': 'E',      '..-.': 'F',
        '--.': 'G',    '....': 'H',   '..': 'I',
        '.---': 'J',   '-.-': 'K',    '.-..': 'L',
        '--': 'M',     '-.': 'N',     '---': 'O',
        '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
     	'...': 'S',    '-': 'T',      '..-': 'U',
        '...-': 'V',   '.--': 'W',    '-..-': 'X',
        '-.--': 'Y',   '--..': 'Z',
        
        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9' 
        }
def exe(message, phone, carrier):
	server = getSMTP()
	message = message.replace('\n', '').replace('\r', '')
	if not (''.join([i for i in message if not i.isdigit()]).replace(' ', '').isalpha()):
		arr = message.split(' ')
		x = ""
		for i in arr:
			if i in codes:
				x+=codes[i]
			else:
				x+="?"
	else:
		x = message

	carriers = {
		'VERIZON': '{0}@vtext.com',
		'ATT': '{0}@txt.att.net',
		'SPRINT': '{0}@messaging.sprintpcs.com',
		'TMOBILE': '{0}@tmomail.net'
	}

	server.sendmail('New message!', carriers[carrier].format(phone), x);

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)