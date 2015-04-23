__author__ = 'marvin'

import configparser, io

def connectionString():
    configuration = configparser.ConfigParser()
    configuration.read('config.cfg')
    return configuration['DEFAULT']['connectionString']

def getProperty(name, section = 'DEFAULT'):
    configuration = configparser.ConfigParser()
    configuration.read('config.cfg')
    return configuration[section][name]


if __name__ == '__main__':
    print(str(getProperty('default', 'MAILS')))
