import smtplib
import os

class NotificationManager:
    def __init__(self):
        self.from_email = os.environ.get("MY_EMAIL")
        self.to_email = os.environ.get("TO_EMAIL")
        self.password = os.environ.get("PASSWORD")
    def send_email(self, iata_code, current_price, new_price):
        price_drop = current_price - new_price
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ.get("MY_EMAIL"), password=os.environ.get("PASSWORD"))
            connection.sendmail(from_addr=self.from_email,
                                to_addrs=self.to_email,
                                msg=(f"Subject: New Lowest Price for {iata_code}\n\n"
                                         f"The price for a trip to {iata_code} has dropped by ${price_drop} from ${current_price} to ${new_price}"))
        print("Email successfully sent")
