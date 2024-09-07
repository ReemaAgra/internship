#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[4]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[6]:


driver=webdriver.Chrome()


# In[7]:


driver.get("https://www.naukri.com/")


# In[9]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")


# In[11]:


designation.send_keys('Data Analyst')


# In[12]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")


# In[13]:


designation.send_keys('Banglore')


# In[14]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")


# In[15]:


search.click()


# In[ ]:




