import time
import asyncio

# I] Run all functions one after other -
# Next function wont get executed before prev gets complete


# II] Run function semi-simaltaneously
# Next function will start executing if prev function has gone for input/output operation


# III] Run functions simultaneously
# Order of display will be amt of time taken by each function, ascendingly