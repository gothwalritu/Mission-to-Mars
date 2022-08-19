#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[ ]:


executable_path = {'executable_path':ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)


# # Visit the NASA Mars News Site

# In[ ]:


# Visit the mars nasa news site

url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[ ]:


# Visit URL

url = 'https://spaceimages-mars.com'

browser.visit(url)


# In[ ]:


# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup

html = browser.html
img_soup = soup(html,'html.parser')
img_soup


# In[ ]:


# Find the relative url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[17]:


executable_path = {'executable_path':ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)


# In[18]:


# 2. Create a list to hold the images and titles.

url = 'https://marshemispheres.com/'
browser.visit(url)


# In[15]:


browser.find_by_text('Sample').first['href']


# In[19]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.

#article= browser.find_by_tag('h3')

hemisphere_image_urls = []  

for i in range (4):
    
    hemispheres = {}
    browser.find_by_css('a.product-item img')[i].click()
    
    html = browser.html

    
    image = browser.find_by_text('Sample').first
    image_url =image['href']
    
    title = browser.find_by_css('h2.title').text
    
    hemispheres["image_url"] = image_url
    hemispheres["title"] = title
    
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
    
        
   
    


# In[ ]:





# In[20]:


# 4. Print the list that holds the dictionary of each image url and title.

hemisphere_image_urls


# In[ ]:


# 5. Quit the browser
browser.quit()


# In[ ]:




