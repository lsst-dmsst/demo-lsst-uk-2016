
from lsst.obs.decam.decamNullIsr import DecamNullIsrTask
config.isr.retarget(DecamNullIsrTask)

config.calibrate.doAstrometry=False
config.calibrate.doPhotoCal=False


