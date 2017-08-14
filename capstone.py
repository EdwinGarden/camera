import time
from myLogger import logSetUp
from cameraActions import cameraAction 

logger = logSetUp()
log = logger.get(__name__)

log.info('log started...')

# camera object test
camera = cameraAction()
camera.takeTimeLapsePhoto()
camera.takeEventPhoto()




