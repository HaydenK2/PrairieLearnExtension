## Summary ##

PrairieLearn can sometimes be a confusing site to navigate. Each course on PrairieLearn can have different grading formats, different categories for
assignments and exams, and thus can often lead to missed deadlines or forgotten assignments if one does not have good organizational habits. PrairieLearn++ is a 
webscraping tool designed to extract the dates from your assignments on PrairieLearn and sort them by most urgent. Such a tool can help students with poor organizational
habits to keep on top of their deadlines by organizing them all into one place.


## Technical Architecture ##

PrairieLearn++ uses the BeautifulSoup python library to webscrape dates and times. This is done in the webscraper.py file. Router.py then uses the data collected from
the webscraper, sorts it, then renders the PrairieLearn++ webpage using the flask python library with the sorted data. The sorted data is then used by the PrairieLearn++
website and turned into boxes storing dates/deadlines.

## Installation Instructions ##

MAKE SURE TO INSTALL THESE PYTHON LIBRARIES FIRST:
- pip install Flask
- pip install beautifulsoup4

To use the application, clone the repository onto your computer and run Router.py to allow the webscraper to work.


## Group Roles ##

- Jerry Liu: co-developed webscraper and websites to webscrape

- Hayden Kim: implemented router.py, PrairieLearn++ (prairielearnplusplus.html) main website functionality 

- Kevin Liu: implemented the custom styling for the project and some of the functionalities of the extension popup

- Andrew Chen: co-developed the webscraper
