import requests
import smtplib
from datetime import datetime
from bs4 import BeautifulSoup

TARGET_PRICE = 60
PRODUCT = "https://www.amazon.com"
MY_EMAIL = "********"
MY_PASSWD = "**************"
DST_EMAIL = "***************"
TODAY = datetime.today().strftime('%Y-%m-%d')

#Get amazon price
http_headers = {
    "User-Agent": "Mozilla/5.0 *******"
}
response = requests.get(url=PRODUCT, headers=http_headers)
response.raise_for_status()
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
product_title = soup.find(name="span", id="productTitle").text.strip(" ")
price_int = soup.find(name="span", class_="a-price-whole").text.strip(",")
price_decimal = soup.find(name="span", class_="a-price-fraction").text
price_string = price_int + "." + price_decimal
product_price = float(price_string)

# #Send email when product price is lower then target price
msg = f"Subject:Amazon Price Alert!!!\n\nIl {product_title} {TODAY} {product_price}€"
if product_price < TARGET_PRICE:
    with smtplib.SMTP("smtp-****") as connection:
        connection.starttls()
        connection.login(user="*********", password=MY_PASSWD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=DST_EMAIL,
                            msg=msg.encode("utf-8")
                            )
