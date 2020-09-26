# kickbaseGiftCollector
With kickbaseGiftCollector you can automate the daily giftcollection by a simple cronjob. It's possibile to log the collection answer with a telegram bot message.
## Requirements
[Python 3.7.5](https://github.com/python), [kickbase_api](https://github.com/kevinskyba/kickbase-api-python/), [telepot](https://github.com/nickoala/telepot)
```
pip3 install telepot
pip3 install Kickbase-API
```
## Usage

    usage: main.py [-h] [--ID ID] [--Ttoken TTOKEN] [--Tuser TUSER] user pw
    
    Python Script for automated collecting gifts at kickbase.com
    
    positional arguments:
      user             E-Mail from kickbase account
      pw               Password from kickbase account
    
    optional arguments:
      -h, --help       show this help message and exit
      --ID ID          Leage ID
      --Ttoken TTOKEN  Telegram Bot Token
      --Tuser TUSER    Telegram Userid

### How2 Get League ID

    >> python main.py email@example.com password
    2020-09-25 22:43:55,373 - kickbaseCollector - INFO - Logged in as KickbaseNick
    2020-09-25 22:43:55,373 - kickbaseCollector - INFO - KickbaseNick Available ID's: 
    2020-09-25 22:43:55,373 - kickbaseCollector - INFO - LeagueName [leagueID]
### Use giftcollector as cronjob
Example for collector bot on a raspberry pi (OS: burster or higher)

 1. place main.py on e.g. desktop 
 2. run cmd
 3. open crontab
    > crontab -e
 4. add new line and exit with saving changes
    ```
    * 0 * * * python3 /home/pi/Desktop/main.py somebody@example.com kickbasepassword --ID kickbaseLeagueID --Ttoken telegramBotToken --Tuser telegramUserid
    ```
 5. wait until cronjob trigger and enjoy.



