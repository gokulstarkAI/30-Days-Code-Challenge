#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyqrcode
import png
from pyqrcode import QRCode


# In[3]:


a = "https://dataelixir.com/"
url = pyqrcode.create(a)
url.png("Qrcode.png", scale = 6)


# In[ ]:




