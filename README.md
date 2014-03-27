venu - The Simplified Valentine Menu
====

The first part of this program parses HTML from http://my.amherst.edu, extracing specifically the menu
(consisting of the breakfast, lunch, and dinner). The scraper program consisted of an analysis element,
where the data was verified for legitimacy (in order to prevent for example, an event named "Lunch", from
being included into the parsed data), and a clean up portion, where the raw data, with it's unorganized 
data in the form a string, was separated into breakfast, lunch and dinner matricies with each array in
the matrix representing a subcategory of food (e.g. Pastries, or Traditional).

The second program of the program involved implementing the Twilio API to incorporate a texting feature for
the program. This can be tested by texting 970-FOOD-441. Upon texting the user will be created with instructions
that inform them of how the service works. From there, you can text 'breakfast', 'lunch', or 'dinner', to
receive a text of the matrix for the specified menu. 

Finally, because the http://my.amherst.edu page is relatively cluttered, I have created in Django, an alternative
website, live here: http://www.venuapp.tabeth.com/valmenu/. This website displays the same data from the scrapper,
but in an easier, simplified format. 


