from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

print("Enter product address:")
url = str(input())
print("Enter your Email address:")
mail=str(input())
print("Enter your password:")
pas=str(input())


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response=requests.get(url,headers=header)

page= response.text

soup = BeautifulSoup(page,"lxml")

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("₹")[1]
a=(price_without_currency[1:].replace(',',''))
final_price=float((a.replace(".",".")))
#final_price = 60000
#print(final_price)

title = soup.find(id="productTitle").get_text().strip()
#print(title)

BUY_PRICE = 75000


if final_price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        message = f"{title} is now at Rs {final_price}"
        connection.starttls()
        result = connection.login(mail,pas)
        connection.sendmail(from_addr=mail,
                        to_addrs=mail,
                msg=f"Subject:Amazon Price Alert!\n\n Your Product is Ready click on the link to Buy :"
                    f"\n\n{message}\n{url}")
