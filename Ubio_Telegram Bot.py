#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time
messages= ['Hi good day, how are you today' ,
           'Great as well, are you aware of this Ukraine vs Rusia war?', 
           'I must say, I am a bit biased towards Ukraine',
           'Because Ukraine is an Independent Country and Invasion can never be ethical in my book', 
           'Allright, so you git the documents?']
answers= ['I am fine and you?' ,
           'Yes I am, but am pretty neutral on the issue, what of you', 
           'Why so?',
           'Well, Mike lets go back to why we are here, I am fed up with the war discussions', 
           'yes here it is']
a=1
while a==1:
    for message,answer in zip(messages,answers):
        base_url='https://api.telegram.org/bot5270140087:AAHJHmE1Azdca2A4iC_BnIFVDOAw0nFS3ak/sendMessage?chat_id=-615047010&text={}'.format(message)
        bas_url1='https://api.telegram.org/bot5165368137:AAHtLCeBF6qr89iE4COLY_jEbEdj2ZOn-kw/sendMessage?chat_id=-615047010&text={}'.format(answer)
        requests.get(base_url)
        time.sleep(3)
        requests.get(bas_url1)
        time.sleep(4)

        
        

    



  


# In[ ]:





# In[ ]:





# In[ ]:




