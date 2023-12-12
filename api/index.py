from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/api')
def index():
    return render_template('index.html')

@app.route('/rsvp', methods=['POST'])
def rsvp():
    name = request.form.get('name')
    rsvp_status = request.form.get('rsvp_status')
    dietary_preferences = request.form.get('dietary_preferences')

    # Store the data in MongoDB
    guest_data = {
        'name': name,
        'rsvp_status': rsvp_status,
        'dietary_preferences': dietary_preferences
    }
    collection.insert_one(guest_data)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
