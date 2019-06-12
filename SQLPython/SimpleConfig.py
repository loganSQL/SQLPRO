# https://docs.python.org/3.4/library/configparser.html#module-configparser

import configparser
config = configparser.ConfigParser()

config['DEFAULT'] = {'Email': 'logansql@outlook.com',
                     'Telephone': '416-9999999',
                     'Github': 'https://github.com/loganSQL'}

config['LoganSQL'] = {'server': 'LoganSQL',
                     'database': 'DBA'}

config['www.alphavantage.co'] = {}
aa = config['www.alphavantage.co']
aa['url'] = 'https://www.alphavantage.co/query?'     # mutates the parser
aa['api_key'] = 'demo'  # same here

#config['DEFAULT']['ForwardX11'] = 'yes'
with open('Exampleconfig.cfg', 'w') as configfile:
  config.write(configfile)