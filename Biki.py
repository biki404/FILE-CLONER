import os, platform
try:
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from biki import reg
    reg()
elif bit == '32bit':
    print "\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools"
