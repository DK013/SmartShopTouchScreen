import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFile, QTextStream
from mainWindow import *
from ManualAddDialog import *
from TouchEventFilter import *
from configobj import ConfigObj
from validate import Validator
from exception import *
from configobj import *
import logging

logger = logging.getLogger(__name__)

def load_stylesheet():
    import style_rc

    f = QFile(":qdarkstyle/style.qss")
    if not f.exists():
        logger.error("Unable to load stylesheet, file not found in resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()
        return stylesheet

def main():
    # Load config spec, config file, and validate the config file with config spec
    configspec = ConfigObj('./configspec.ini', raise_errors=True, _inspec=True)
    validator = Validator()

    config = ConfigObj('./config.ini', configspec=configspec, create_empty=True)
    errors = config.validate(validator, preserve_errors=True, copy=True)

    # Check and report any errors that occurred when validating config file
    msg = ""
    for entry in flatten_errors(config, errors):
        [sectionList, key, error] = entry

        if key is not None:
            sectionList.append(key)

        # Parameter name is each section joined by an arrow(->) followed by the value
        # So one->two would be the value two in the section one
        parameterName = '->'.join(sectionList)

        # An error of false means the section/value was missing, otherwise error is an exception with a string describing error
        if error is False:
            msg += "%s: Missing value or section\n" % parameterName
        else:
            msg += "%s: %s\n" % (parameterName, error)

    if len(msg) > 0:
        # An error occurred, save the config file in case any default data was copied
        config.write()
        raise SmartShopException("Could not parse config file:\n%s" % msg)

    # Create application
    app = QApplication(sys.argv)

    # Create a filter for touch screen events
    touchFilter = TouchEventFilter()
    app.installEventFilter(touchFilter)

    # Load the stylesheet content from resources
    app.setStyleSheet(load_stylesheet())


    # TODO Start by coding in the concept GUI to start out
    # TODO Implement the buttons in the concept GUI

    form = MainWindow(config)

    # Will pass this argument in Raspberry Pi 3 to get fullscreen display
    if "-fullscreen" in sys.argv:
        constants.fullscreen = True
        form.showFullScreen()
    else:
        constants.fullscreen = False
        form.show()

    # Execute application and retrieve return value when done
    ret = app.exec()

    # Save config file. It is possible for changes to be made using settings menu in GUI
    config.write()

    # Exit python with return value from application execution
    sys.exit(ret)

if __name__ == '__main__':
    main()
