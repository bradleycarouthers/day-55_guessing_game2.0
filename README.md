# day-55_guessing_game2.0
Day 55 of 100 
html_and_url_parsing

More on decorators and Flask usage. Made a server and from there made an upgraded version of the guessing game I did like 40 days ago haha.
The user guess goes in the URL path "/<int:guess>"(an integer), at the end of the URL address. Used random.randint(n1, n2) to generate a number to be held by the answer variable.

Depending on whether the guess was too low, too high, or correct will determine the color of the h1 tag and which gif is displayed.

Overall basic stuff, but building a foundation one step at a time.
