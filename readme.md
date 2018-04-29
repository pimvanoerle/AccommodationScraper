Accommodation scraper.

This scraper is focused on scraping airbnb, but
can be extended for more generic usage.

Written in Python as it's a language that's easy to find people to work on, as key to this system is ease of writing scrapers. 

The three pages this was built to scrape are:
https://www.airbnb.co.uk/rooms/14531512?s=51
https://www.airbnb.co.uk/rooms/19278160?s=51
https://www.airbnb.co.uk/rooms/19292873?s=51


Things left to do for an MVP version:

General stuff
* Logging: add logging - we should log to at least a rotating file (ideally to a central spot)
* Logging: add some log levels so we can differentiate between info, debug, error, warn etc.
* Logging: add more info to exceptions and logging points to make them more usable
* add metrics - we should fire off events on:
    * initiation
    * completion (and time the bits took)
    * errors
    * queue of waiting requests, so that we can trigger autoscaling etc
* Scaling: pull configuration into a config file so we can treat configuration as code (version, review, roll out green/blue etc)
* Scaling: modify API to push back once a limit of the internal queue is hit, so that we can implement a back-off approach.
* set up release pipeline to spin up instances of this scraper. Think of: 
    * running the various (unit, integration, etc) tests, 
    * green/blue or canary deployment based on metrics in prod, 
    * autoscaling based on metrics from the fleet, 
    * having a deployment pipe for config as well as code) 
* Tests: add integration tests, as there are none right now
* Tests: run on production target VMs or functions/lambda and check (with locust.io or other) what throughput is so we can size better.
* extend the small API to have more functionality
* make asynchronous work in a better way
* Localization: deal with localization of the one key thing that could be localized for this simple thing - the property name

Specific to Scraper:
* find a better way to register Connectors when written (now need to add new type in a different file, which is simple but could be forgotten)
* extend Accommodation Types to be a more generic list (currently just what's needed for AirBnB)

Things to think about:
* this design is predicated on running cheap instances in AWS Lambda or the like. Cost should be a major consideration in where this should run, as that approach will get very costly at scale (and something like re-writing in an Actor pattern in Java/Akka could work well for that)