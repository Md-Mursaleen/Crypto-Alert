# Crypto-Alert
This Python script will help you get E-Mail alerts following certain conditions like the price going over a threshold (Example: Price > 2000 USD --> Alert)

Befor using the file you will need to follow these steps:
* Create a Gmail Account and set it up
* Create an account cryptomarketcap.com to get an API KEY
* Entrer the above info in your main.py
* DONE !

First, create a Gmail Account and go to this link : https://shorturl.at/dySY4 . Once there, accept less secure apps !

Secondely, go to https://coinmarketcap.com/api/ . And create an Account. After you complete all verification, go to the dashboards and copy your API KEY

![Image of the dashboard](https://github.com/saadze/Crypto-Alert/blob/main/images/coinmarketKEY.PNG)

Now you are almost ready to get up  and running, the basic file will only fetch the price of a currency after a certain time and send an email, but if you want to add conditions such as thresholds you can !

Let me guide you through this:
1. Open main.py
2. Add the email adress that you created + its password
3. Change the "to" variable to your main email adress (where you will receive alerts)
4. Set a subject for the E-mails and set time to the time between the requests (in seconds) !!! 333 Calls per day MAX!
5. Finally set the symbol of the currency you want to follow in the symbol variable (example: BTC,ETH,XRP,LTC,DOGE ...)
![Image of the variables to change](https://github.com/saadze/Crypto-Alert/blob/main/images/variables.PNG)
