import logging

class logSetUp:
    def get(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.DEBUG)

        # create a file handler for the logs
        fh = logging.FileHandler('logs.log')
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        log.addHandler(fh)

        log.info('Logger set up')
        return log

