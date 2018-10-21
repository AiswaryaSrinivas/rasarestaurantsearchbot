from .chatBotConfigParser import ChatBotConfigParser
import logging
import os
import tempfile
from datetime import datetime

class ChatBotLogging:
    def __init__(self):
        configParserObj = ChatBotConfigParser().parser
        self.logger = logging.getLogger("ChatBotBase")
        
        # Just keeping it as default #
        self.logLevel = logging.DEBUG 
        
        # Set Log Level #
        if configParserObj.get('ChatBotLogging','logLevel') == "DEBUG":
            self.logLevel = logging.DEBUG
        elif configParserObj.get('ChatBotLogging','logLevel') == "INFO":
            self.logLevel = logging.INFO
        elif configParserObj.get('ChatBotLogging','logLevel') == "ERROR":
            self.logLevel = logging.ERROR
        elif configParserObj.get('ChatBotLogging','logLevel') == "CRITICAL":
            self.logLevel = logging.CRITICAL
        else:
            raise("Unknown Log Level provided")
        
        self.logger.setLevel(self.logLevel)
        
        # Build a log formatter #
        formatter = logging.Formatter('%(asctime)s : %(name)-32s : %(threadName)s : %(process)d : %(message)s')
        
        # Create file handler logger #
        log_location = configParserObj.get('ChatBotLogging','logPath')
        if os.path.isdir(log_location):
            log_file = os.path.realpath(os.path.realpath(log_location) + "/" + "ChatBot.log")
        else:
            log_file = os.path.realpath(os.path.realpath(tempfile.gettempdir()) + "/" + "ChatBot.log")
        print(datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + " : ChatBot : Message : " + "Log File = " + log_file)
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        fh.setLevel(self.logLevel)
        
        #ch = logging.StreamHandler()
        #ch.setLevel(self.logLevel)
        #ch.setFormatter(formatter)
        
        # register handlers with main logger obj #
        self.logger.addHandler(fh)
        #self.logger.addHandler(ch)
        
        self.logger.info("---- Started Logging Framework ----")
    def getLogger(self):
        return(self.logger)
        

# Build a singleton object here #
def __globalinit():
    return ChatBotLogging()

global ChatBotLoggingGlobalObj
ChatBotLoggingGlobalObj = __globalinit()