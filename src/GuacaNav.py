#!/usr/bin/python3

import json
import sys
from GuacaGui import Gui

def main():
    configFile = open("config.json", "r")
    configString = configFile.read()
    configJson = json.loads(configString)
    configFile.close()
    mainWindow = Gui(configJson)

if __name__ == "__main__":
    main()
