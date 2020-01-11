import os

# Making channel list file, if it not exist.
if not os.path.exists('.setting'):
    print('Made setting file.')
    with open('./.setting','w') as f:
        pass