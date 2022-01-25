# Two Wheels - 🚧 (Work in Progress)
A Python code base responsible for scraping PinkBike Buy / Sell posts Bike data (sorry PinkBike). Information gathered from Bike posts will be used to train a machine learning
model capable of estimating the price of a bike given some features. The goal of this project to eventually build a python backend (Flask) that can deliver Bike data 
via RESTful API and offer machine learning predictions given a set of bike specs. 

# MVP Milestone 
I love to mountain bike, so the scope of this project is limited to the [All Mountain / Enduro](https://www.pinkbike.com/buysell/list/?region=5&category=2) bike category on pink bike. Sorry to all the road pedal heads ;)

MVP milestone will include the following features:
- ✔️ Flask SQLAlchemy and Flask-migrate integration for easy domain object development
- ✔️ Setup unit tests for Flask app (this was a tedious process to learn)
- ✔️ A pink bike crawler for navigating through Buy / Sell pages, that uses a patience factor to not overload their servers!!
- ✔️ A BeautifulSoup web scraper for accessing the bike data
- ✔️ Data driven Bike model discovery (see notebooks for the analysis)
- 🔲 A data processing pipeline for cleaning scraped data from PinkBike 
- 🔲 A simple machine learning model that predicts the price of a bike
- 🔲 Functioning FLASK app with a single endpoint for POST machine learning predictions

My [Issue Board](https://github.com/djcurill/two-wheels/issues) is pretty religiously maintained, so to see the current state of the project, I recommend starting there. If you are a KanBan lover, check out the [MVP Project Board](https://github.com/djcurill/two-wheels/projects/1) instead.

With an MVP release, the machine learning model will use the following set of features to predict the price:
- The year of manufacturing
- The Brand
- The model
- The condition / quality
- The material
- The frame size (should have no impact to be honest)
- The wheel size
- The front suspension travel
- The rear suspension travel

# Assumptions & Limitations

## Bike Tiers
Most of the assumptions lie around the complexity of the bike scraper. Large mountain bike companies offer far too many products (IMO), so there are
so many different *tiers* to a single Bike Model. For example, Norco has C1, C2, C3 etc... to mark different tiers of their Carbon material (Rolls eyes). Scraping this
data and adding that logic to the data model will be a tough cookie.

## Bike Brand to Model Mapping
I currently use a pretty simple data pipeline to identify popular bike models for each bike brand. If you have a look at the PinkBike Buy / Sell Posts for mountain bikes, you will begin to notice a pattern. Here a couple of examples:
* 2016 Commencal META AM V4 BIk. Edition
* 2020 Niner Jet 9 RDO 4 Star
* 2016 Giant Anthem Advanced 1 27.5 1 Medium

As you can see, the general pattern looks something like:
> [Year] [Brand] [Model] [... total crapshoot follows]

The analysis I use to identify popular models uses large numbers to my advantage. It uses regular expressions to split the title on a word match with a brand name. I then
take the first item to follow after the Brand, and that is more often than not the model of the bike. Typically patterns will emerge from the noise, and I use the 
marvellous `Counter` function from python to indentify most common bike models for each bike. The results of my analysis were then transcribed to the `bikes.json` file stored
in the root directory.

Future stages of this project will deal with handling the total shit show that follows the Bike Model of the title. Looking forward to it 🙈

## Bike Upgrades
Many pedal heads will totally deck out their rides with the latest and greatest gear. My current model will not handle that edge case. Will need to build out NLP use cases
that extract key words from titles and descriptions to determine the upgrades / modifications riders have applied to their kit.

# Future Work / Wish List 

## Front End
No project is complete without a frontend. I look forward to building a React / Redux front end that enables a user to enter their bike specs and receive a 
machine learning prediction that estimates the price of their bike.

## Machine Learning & Data Scraping
So many wishlists here, will have to break it down to bullet point form:
1. Extract bike tier information from the title
2. Key word extraction of bike descriptions using Natural Language Processing. Use NLP derived tags as model features.
3. Computer vision problem on bike photos to detect bike quality factor 🤯 (maybe sell it to pink bike as a service hehe)

Unfortunately, a lot of these goals will cost $$$ to fund data storage of photos, and unstructured text descriptions. :( 

## CI / CD
Setup CI / CD pipelines for unit and integration tests. Don't see this being too hard. 
