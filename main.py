from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random, time

Level = [ # (difficutly, dimensions, # of mines)
  ("Easy", 8, 10), 
  ("Medium", 16, 40),
  ("Hard", 24, 99)
]

# colorcodes the number of touching objects 
NUM_COLORS = {
  1: QColor('#f44336'),
  2: QColor('#9C27B0'),
  3: QColor('#3F51B5'),
  4: QColor('#03A9F4'),
  5: QColor('#00BCD4'),
  6: QColor('#4CAF50'),
  7: QColor('#E91E63'),
  8: QColor('#FF9800')
}

