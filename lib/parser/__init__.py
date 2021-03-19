try: 
    from bs4 import BeautifulSoup
except:
    import os 
    os.system('pip3 install bs4')
    os.system('clear')
    print("Was installed bs4 module.")
    del os
