import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    from biki import main_apv
    main_apv()
elif bit == '32bit':
    print "\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools"
