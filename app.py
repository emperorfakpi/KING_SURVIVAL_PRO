from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, static_folder='assets',template_folder='templates')

# Your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = '7377509769:AAF9uJ1kRFAHQkio80h2xfykDkh3Pcpekx4'
CHAT_ID = '1803335709'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Get data from the form submission
    section = request.form.get('section')
    book_id = request.form.get('bookId')
    book_name=request.form.get('bookName')
    user_name = request.form.get('userName')
    user_email = request.form.get('email')
    user_phone = request.form.get('phone')
    index_number = request.form.get('indexNumber')
    unique_code = request.form.get('uniqueCode')

    # Format message to be sent to Telegram
    message = (
        f"New Reservation Request:\n"
        f"Unique Code: {unique_code}\n"
        f"Section: {section}\n"
        f"Book name: {book_name}\n"
        f"Book id: {book_id}\n"
        f"User Name: {user_name}\n"
        f"email: {user_email}\n"
        f"User phone: {user_name}\n"
        
        f"Index Number: {index_number}"
    )

    # Send message to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(telegram_url, data=payload)

    if response.status_code == 200:
        return jsonify({"status": "success", "message": "Request sent to Telegram."}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to send request to Telegram."}), 500

if __name__ == '__main__':
    app.run(debug=True)
 