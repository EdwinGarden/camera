from myLogger import logSetUp

class cameraAction:
    
    logger = logSetUp()
    global log
    log = logger.get(__name__)
    
    def takeTimeLapsePhoto(self):
	log.debug('take a time lapse photo')
        
    def takeEventPhoto(self):
        global log
        log.debug('take a motion event photo')

        
