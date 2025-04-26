from flask import Flask, render_template, request
import os
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

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

    # # Send email to admin
    # try:
    #     admin_email = "admin@example.com"  # Replace with your admin email
    #     sender_email = "your-email@example.com"  # Replace with your email
    #     sender_password = "your-email-password"  # Replace with your email password

    #     subject = "New Land Inquiry"
    #     body = f"""
    #     New Inquiry Details:
    #     Name: {name}
    #     Email: {email}
    #     Phone: {phone}
    #     Requirements: {requirements}
    #     """

    #     # Create email message
    #     msg = MIMEMultipart()
    #     msg['From'] = sender_email
    #     msg['To'] = admin_email
    #     msg['Subject'] = subject
    #     msg.attach(MIMEText(body, 'plain'))

    #     # Send email
    #     with smtplib.SMTP('smtp.gmail.com', 587) as server:
    #         server.starttls()
    #         server.login(sender_email, sender_password)
    #         server.send_message(msg)
    #     print("Email sent successfully!")
    # except Exception as e:
    #     print(f"Failed to send email: {e}")

    # # Record data in Google Sheets
    # try:
    #     # Define the scope and authenticate
    #     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    #     creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)  # Replace with your credentials file
    #     client = gspread.authorize(creds)

    #     # Open the Google Sheet
    #     sheet = client.open("Land Inquiries").sheet1  # Replace with your Google Sheet name

    #     # Append the data
    #     sheet.append_row([name, email, phone, requirements])
    #     print("Data recorded in Google Sheets!")
    # except Exception as e:
    #     print(f"Failed to record data in Google Sheets: {e}")

    # Render thank you page
    return render_template('thankyou.html', name=name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 
    # app.run(debug=True)
