from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import *

# This file contains all the constants that will not be regularly changed upon runtime
# It is benficial to developers who want to fine-tune or tweak some parameters to optimize some aspect of the code

# Enables/Disables the barcode scanner device. If enabled, this will actually search for the barcode scanners on the USB
# ports and try to connect with them. Only disable this for developer mode where the barcode scanners will not be used
barcodeScannerDeviceEnable = True

# Enables/Disables shortcuts for the barcode scanner. If enabled, this will allow the user to press Ctrl+1 and Ctrl+2
# which enables an input dialog box to input the barcode to be sent.
barcodeScannerShortcut = True

# Geometry for each window that is going to be displayed
windowGeometry = QRect(0, 0, 800, 480)

# Interval for polling barcode scanners in milliseconds
scannerPollInterval = 5

# Interval for updating recommended items in milliseconds
updateRecommendedItemsInterval = 5000

# Whether the menu will be shown as full screen or not
fullscreen = False

# number of years after current year for expiration date
maxExpirationYear = 25

# Database information to connect to PostgreSQL server.
dbDatabase = "smartshop"
dbUsername = "jacob"
dbPassword = "password"
dbHost = "addison404project.ddns.net"
dbPort = "5432"

# Maximum length that a category name can be
maxCategoryNameLength = 20

# Maximum length that an item name can be
maxItemNameLength = 20

# Floating Push Buttons on Main Page to Remove Items from Shopping Lists
removeReqShoppingItemBtnGeometry = QRect(280, 390, 58 + 12, 58 + 12)
removeRecShoppingItemBtnGeometry = QRect(634, 390, 58 + 12, 58 + 12)
removeMoveToReqListBtnGeometry = QRect(576-12, 390, 58 + 12, 58 + 12)

# The time of day where the usage rate will be calculated on a day by day basis
# Order is hour, minutes, and seconds. They should be normalized between their normal values (e.g. hour between 1 and 23)
usageRateTime = time(hour=0, minute=10, second=0)

# Log filename, where information will be stored
logFilename = 'log.txt'
import logging
logLevel = logging.DEBUG