#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

# A fichero NUEVO cada vez
## logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# Config. con timestamp
## logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logging.warning('is when this event was logged.')

# Formateado de cadenas
logging.warning('%s before you %s', 'Look', 'leap!')
x, y = 'Look', 'leap!'
logging.warning(f'{x} before you {y}')
