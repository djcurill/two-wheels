# Two Wheels - 🚧 (Work in Progress)
---
A Python code base responsible for scraping PinkBike Buy / Sell posts Bike data (sorry PinkBike). Information gathered from Bike data will be used to train a machine learning
model capable of estimating the price of a bike given some features. The goal of this project to eventually build a python backend (Flask) that can deliver Bike data 
via RESTful API and offer machine learning predictions given a set of bike specs. 

# MVP Milestone 
---
I love to mountain bike, so the scope of this project is limited to the [All Mountain / Enduro]() bike category on pink bike. Sorry to all the road pedal heads ;)

MVP milestone will include the following features:
- [ ] Functioning FLASK app with a single endpoint for POST machine learning predictions
- [ ] Flask SQLAlchemy and Flask-migrate integration for easy domain object development
- [ ] Setup unit tests for Flask app (this was a tedious process to learn)
- [ ] A pink bike crawler for navigating through Buy / Sell pages, that uses a patience factor to no overload their servers
- [ ] A data processing pipeline for cleaning scraped data from PinkBike 
- [ ] A simple machine learning model that predicts the price of a bike

My [Issue Board](https://github.com/djcurill/two-wheels/issues) is pretty religiously maintained, so to see the current state of the project, I recommend starting there. If you are a KanBan lover, check out the 
[MVP Project Board](https://github.com/djcurill/two-wheels/projects/1) instead.

## Assumptions & Limitations
---

