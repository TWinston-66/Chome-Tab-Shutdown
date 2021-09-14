import webbrowser
import time
    
i = 0
while True:
    time.sleep(2)
    url = 'https://www.google.com'
    webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    i = i + 1
    print('Tab #')
    print(i)
