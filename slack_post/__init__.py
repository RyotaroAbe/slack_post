import os

libdir = os.path.dirname(__file__)
stgFilePath = libdir + '/.setting'
# Making channel list file, if it not exist.
if not os.path.exists(stgFilePath):
    print('Made setting file.')
    with open(stgFilePath,'w') as f:
        pass
    