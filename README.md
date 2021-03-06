# Facebook friends pull

Clone this repository:

```bash
$ git clone https://github.com/YanNovikov/Generator-exchange-orders.git
```

Additional modules:
```bash
$ pip install -r /path/to/project/folder/requirements.txt 
```

Meet, friends pull
--
You have to install the latest version of Google Chrome: https://www.google.ru/chrome/

It works automatically:
* First of all browser starts working
* Secondly you are signed in Facebook
* Finally you have a list of your friends with Names and Links to profiles


You can set credentials in configurations. Example is defaults.json in dirrectory files/

---
#How to use?

## Start app

```
$ python launcher.py -c --loggermode=info --configs customconfigs.json
```

--loggermode it is a level of output logs. Can be: trace, debug, info, warning, error, critical, fatal.

-f file writing logs.

-c console writing logs.

--configs is a path to your config file.

All options are not required.
By default is info level, console and file writing, defaults.json


---
## See result
```bash
$ python launcher.py --loggermode=debug
[LOGGER]: Started with default settings.
[LOGGER]: Logger mode is now set to debug.
[LOGGER]: Logger output goes to file files/logs/Thu May  2 16:13:21 2019.
[INFO]: Initializing application...
[INFO]: Loading configs from files/defaults.json.
[DEBUG]: Read from files/defaults.json - Success
[INFO]: Configurations for selenium loaded.
[INFO]: Initializing completed.
[DEBUG]: Login is set
[DEBUG]: Password is set
[DEBUG]: Button is clicked
[INFO]: Sign in - Success
[DEBUG]: Click profile
[DEBUG]: Click friends
[DEBUG]: Pulling friends info
[INFO]: Information is collected - Success
[INFO]: Names and links:
[INFO]: 

Дмитрий Корчевский
https://www.facebook.com/dkorchevskyy?fref=pb&hc_location=friends_tab

Дарина Косарева
https://www.facebook.com/RINA9914?fref=pb&hc_location=friends_tab

Дария Кердывар
https://www.facebook.com/profile.php?id=100017239297886&fref=pb&hc_location=friends_tab

Vladislav Naugolny
https://www.facebook.com/vladislav.naugolny.1?fref=pb&hc_location=friends_tab

Света Коваленко
https://www.facebook.com/profile.php?id=100017230869325&fref=pb&hc_location=friends_tab

Дмитрий Фурсов
https://www.facebook.com/profile.php?id=100007429994423&fref=pb&hc_location=friends_tab

Maxim Starchenko
https://www.facebook.com/profile.php?id=100004798605429&fref=pb&hc_location=friends_tab

Саша Власенко
https://www.facebook.com/sasha.vlasenko3?fref=pb&hc_location=friends_tab

Елена Маршуг
https://www.facebook.com/elena.marshug?fref=pb&hc_location=friends_tab

```