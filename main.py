import os
from model.load_model import load_pretrained_model, forecast_plant_health
from sensors.sensor_data import read_sensor_data
from sklearn.preprocessing import MinMaxScaler
import smtplib
from twilio.rest import Client

# Load model and scaler
model = load_pretrained_model('model/lstm_model.h5')
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit([[20, 30, 0.1], [35, 90, 1.0]])  # Example scaling based on sensor range

# Twilio SMS setup
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

def send_sms_alert(message, to_number):
    """Sends an SMS alert using Twilio."""
    try:
        message = client.messages.create(
            body=message,
            from_='+your_twilio_number',
            to=to_number
        )
        print(f"Alert sent successfully: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

def send_email_alert(subject, body, to_email):
    """Sends an email alert."""
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'your_email@gmail.com'
        sender_password = 'your_password'
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender_email, to_email, msg)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def check_plant_health_and_alert(to_number, to_email):
    """Check plant health and send alerts if issues are detected."""
    sensor_data = read_sensor_data()  # Get sensor data
    health_status = forecast_plant_health(sensor_data, model, scaler)
    
    if health_status == 'Diseased':
        # Trigger alerts
        send_sms_alert("ALERT: Plant is showing signs of disease.", to_number)
        send_email_alert("Plant Disease Alert", "The system detected a disease. Please take action.", to_email)
    
    print(f"Plant Health: {health_status}")

# Main execution
if __name__ == '__main__':
    to_number = '+1234567890'  # Farmer's phone number
    to_email = 'farmer_email@example.com'  # Farmer's email address
    
    check_plant_health_and_alert(to_number, to_email)
