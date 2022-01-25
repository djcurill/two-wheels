# Two Wheels - 🚧 (Work in Progress)
A Python code base responsible for scraping PinkBike Buy / Sell posts Bike data (sorry PinkBike). Information gathered from Bike data will be used to train a machine learning
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
take the first item to follow after the Brand, and that is more often than not the model of the bike. 

Future stages of this project will deal with handling the total shit show that follows the Bike Model of the title. Looking forward to it 🙈
