#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python Script for automated collecting gifts at kickbase.com
"""

import argparse
import os
import sys
import subprocess
from kickbase_api.kickbase import Kickbase as kb
import logging
import datetime
import time
import telepot

__author__ = "LukasFritz"
__copyright__ = "Copyright 2020, LukasFritz"
__credits__ = ["https://github.com/LukasFritz"]
__license__ = "MIT" 
__version__ = "0.0.1"
__maintainer__ = "Lukas Fritz"

logger = logging.getLogger("kickbaseCollector")
logger.setLevel(logging.DEBUG)
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Python Script for automated collecting gifts at kickbase.com')

# Positional Arguments
parser.add_argument('user',
                    help="E-Mail from kickbase account",
                    type=str)
parser.add_argument('pw',
                    help="Password from kickbase account",
                    type=str)
#optional Arguments
parser.add_argument('--ID',
                    help="Leage ID",
                    type=str)
parser.add_argument('--Ttoken',
                    help="Telegram Bot Token",
                    type=str)
parser.add_argument('--Tuser',
                    help="Telegram Userid",
                    type=str)

args = parser.parse_args()

def login(main):
    try:
        user,leagues = main.login(args.user,args.pw)
        logger.info("Logged in as %s", user.name)
        return user, leagues
    except:
        logger.info("Login for %s failed!", args.user)

def sendTelepotMessage(message):
    bot = telepot.Bot(args.Ttoken)
    bot.sendMessage(args.Tuser, message)

def main():
    kba = kb()

    if args.ID is None:
        user, leagues = login(kba)
        logger.info("%s Available ID's:", user.name)
        for league in leagues:
            logger.info("%s [%s]", league.name, league.id)
    else:
        user, leagues = login(kba)
        i = 0
        while True:
            answer = kba.league_collect_gift(args.ID)
            if not answer:
                break
            i = i + 1
        
        if i >= 1:
            logger.info(str(i) + " Gift collected!")
            sendTelepotMessage("League["+ args.ID +"]: "+ str(i) + " Gift collected")
        else:
            logger.warning("No Gift collected!")
            sendTelepotMessage("League["+ args.ID +"]: No Gift collected!")


if __name__ == '__main__':
    main()