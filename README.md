[![Discord](https://s15.postimg.cc/hb3hne1jf/banner.png)](http://discord.gg/8nG3FkS)

<p align="center">
  <b>Suggestion Bot</b><br>
  <a href="http://discord.gg/8nG3FkS">Support</a> |
  <a href="http://paypal.me/derpdays">Donate</a> |
  <a href="https://discord.gg/r3sSKJJ">Python Support</a>
  <br><br>
</p>

---

### The bot as is without modification contains:
* Custom output locations
* Enable/Disable command
* Ask the questions in private messages or in the channel the command was executed from
* Automatic config generation
* Ability to change where the suggestions get posted


### Installation

Suggestion Bot is built off the discord.py and requires python 3.6 to be installed and for some some requirements to be installed.

Install the following dependencies for the bot to work!


- PYTHON V3.6
- GIT

---

Download the [latest](https://www.python.org/downloads/) version of python and make sure select `Add Python 3.X to PATH`.

---

Download the [latest](https://git-scm.com/download/win) version of git and make sure to select `Run git from the windows command prompt`.

---

Right click in the folder you want the bot to be in and click `Git Bash Here`
Then copy the following into the terminal:
- `git clone https://github.com/DerpDays/Suggestion-Bot.git`
- `pip install -r requirements.txt`


Run the setup.bat and enter your [bots token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) and click `SUBMIT TOKEN` then decide if you want the bot to auto-restart (RECCOMENDED) or if you want the bot to not auto restart then click on the button that matches your decision.

Add the bot to your server by using this link https://discordapp.com/api/oauth2/authorize?client_id=YOURBOTCLIENTID&permissions=8&scope=bot but replacing YOURBOTCLIENTID with your bots **client id**.

The bot should be ready to start now if you entered a correct token, run startbot.bat and then use `!bot prefix` to set a global prefix and then configure the bot with `!settings`!


> Did you put a invalid bot token? Dont worry because theres a simple fix without redownloading the bot all over again. Open settings.json and under the `"GLOBAL"` object find `"TOKEN":` and replace the content after the `:` with "YOURBOTTOKEN"!

### Todos

 - Messages able to be changed via discord.
 - Per server messages.

# License

Released under the [MIT](https://en.wikipedia.org/wiki/MIT_License) License.

MIT License

Copyright (c) 2018 DerpDays

>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
