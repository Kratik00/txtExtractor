#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7808401304:AAEL0sywIAymVv6LUzSgOpxyWuzM70tSsRM")
    API_ID = int(os.environ.get("API_ID", "25017900"))
    API_HASH = os.environ.get("API_HASH", "3830600881a164826e60f2806b28e666")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7145429939")
