# NEA Telegram Bot

This is a telegram bot that communicates with NEA Api to provide realtime data on the move !

### Prerequsite

  1. **Python 2.7 and above**
  2. **NEA Api Key** 
  3. **Telegram Bot Token**

 - *NEA Api keys can be generated **[here][nea]***
 - *How to create your own **[telegram Bot][botfather]***


### Installation

Install **lxml**,  **pygame** and **requests** libraries
```sh
sudo pip install lxml
sudo pip install pygame
sudo pip install requests
```
### Running the Bot
CD to root of NEA Bot folder
```sh
cd ~/path/neaBot
```
Create **token_NEA.txt** file and insert NEA Api key
```sh
echo >> token_NEA.txt <Nea Key> 
```
Create **token_telegram_bot.txt** file and insert Telegram Bot Token
```sh
echo >> token_telegram_bot.txt <Bot Token> 
```
Run the **nea_main_bot.py** script
```
python nea_main_bot.py
```


##### *The bot should be running and can be accessed by searching for the bot in telegram, start a query by sending /start to the bot* 





   [nea]: <https://www.nea.gov.sg/api/api/nea-s-datasets#Register>
   [Botfather]: <https://core.telegram.org/bots>

