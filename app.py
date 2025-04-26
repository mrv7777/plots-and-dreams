from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listings')
def listings():
    return render_template('listings.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/get-quote', methods=['POST'])
def get_quote():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    requirements = request.form.get('requirements')
    print(f"New Inquiry: {name}, {email}, {phone}, {requirements}")
    return render_template('thankyou.html', name=name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 
