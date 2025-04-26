from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-quote', methods=['POST'])
def get_quote():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    requirements = request.form.get('requirements')
    
    # Here you would normally save data to database or send an email
    print(f"New Inquiry: {name}, {email}, {phone}, {requirements}")

    return render_template('thankyou.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
