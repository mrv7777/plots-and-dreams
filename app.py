from flask import Flask, render_template, request

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
    app.run(debug=True)
