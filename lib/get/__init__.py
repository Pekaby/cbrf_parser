try: 
    import requests
except:
    import os 
    os.system('pip3 install requests')
    os.system('clear')
    print("Was installed requests module.")
    del os
