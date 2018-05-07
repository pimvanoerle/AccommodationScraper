## Accommodation scraper.

This scraper is focused on scraping airbnb, but can be extended for more generic usage.

Written in Python mainly as it's a language that's easy to find people to work on, as key to this system is ease of writing scrapers. See below for some thoughts around suitability for large scale systems :)

The three pages this was built to scrape are:
https://www.airbnb.co.uk/rooms/14531512?s=51
https://www.airbnb.co.uk/rooms/19278160?s=51
https://www.airbnb.co.uk/rooms/19292873?s=51

The last one seems to have been pulled (as of 6th May), so changed it for a different one:
https://www.airbnb.co.uk/rooms/16141909?s=51

AioHTTP is used as an http server as a nod to the need for this sort of operation to be asynchronous, but proper asynchronous behaviour is not fully built out for this test.

### Usage

Written for Python3, see requirements.txt for the packages used (beautifulsoup and aiohttp).

There are two modes in which the thing can operate - by instantiating the simple Scraper class for one-off instances (mostly for testing), and properly by running the async web server in /Server/main.py

To do so from, please do the following:

make sure to be using python3 with pip installed

if virtualenv is not installed: pip3 install virtualenv

in the root directory of the project (with server.py and requirements.txt etc), do:
* create a virtualenv: python3 -m virtualenv env
* activate virtualenv: source env/bin/activate
* install the requirements pip install -r requirements.txt
* run the server: python server.py

* in a different terminal, navigate to the same project root folder
* activate virtualenv: source env/bin/activate
* run the client tester: python scrape_three.py

That opens a little web server on 127.0.0.1:8081. To call, do the following:
POST to 127.0.0.1:8081/accommodation, with as payload some json containing a URL field
like {"url": "https://www.airbnb.co.uk/rooms/14531512?s=51"}

that will return a serialized version of the Accommodation page that was requested, again as JSON.

**To just see output on the console without any client/server interaction, run test_airbnb_3_cases_can_be_parsed in integration_tests.py.**

### small note on amenities (and fragility)

Note that this uses the various HTML elements on the page to fish out the data, so it's pretty fragile when change happens, and it can only fish out the 6 amenities that are on the page. AirBNB does stuff their pages with a large json blob with all data, so a solution to get all amenities would be to parse that rather than the rendered elements (doesn't make it less fragile, but at least gets all amenities). Other option is to reverse engineer the amenities details call, and force that call to be made to scrape the data from the rendered overlay.

### Work left to do to make it POC worthy:
* should make a little config file for ease of changing airbnb values, server values etc. Add AirBnB and server config to that. This would take any hardcoded config out of the code, which is good.
* add some rudimentary logging (rotating so that stuff doesn't fill disk up quietly)
* flesh out the rate limiter for the airbnb scraper so that we don't spam too much
* revisit the unit tests and make sure key behaviours are covered
* asynchronicity is only at the Web Server level - the actual call to scrape is still happily blocking. This needs to be fixed, can just use aiohttp's client, which should be good enough (also look at how long the parse step takes and spin that off as well)

### Things left to do for a proper MVP version, and some other considerations

#### Logging and Metrics
* Logging: add logging - we should log to at least a rotating file (ideally to a central spot)
* Logging: add some log levels so we can differentiate between info, debug, error, warn etc.
* Logging: add more info to exceptions and logging points to make them more usable
* add metrics - we should fire off events to some sort of metrics server (Cloudwatch?) on:
    * initiation
    * completion (and time the bits took)
    * errors
    * queue of waiting requests, so that we can trigger autoscaling etc

#### Deployment and Configurability
* Scaling: pull all configuration into a config file so we can treat configuration as code (version, review, roll out green/blue etc)
* Scaling: modify API to push back once a limit of the internal queue is hit, so that we can implement a back-off approach.
* set up release pipeline to spin up instances of this scraper. Think of:
    * running the various (unit, integration, etc) tests,
    * green/blue or canary deployment based on metrics in prod,
    * autoscaling based on metrics from the fleet,
    * having a deployment pipe for config as well as code

#### Tests
* Add integration tests, as there are only a couple noddy ones right now
* Add Unit Tests to the untested bits (mainly the little http server)
* StressTest: run on production target VMs or functions/lambda and check (with locust.io or other) what throughput is so we can size better.

* for Unit Tests: mock out the responses and endpoints, so that we don't always have to call the actual target (much cleaner, but also another layer of indirection that can hide issues)

#### Extra bits to do to
* Extend the small API to have more functionality
* Localization: deal with localization of the one key thing that could be localized for this simple thing - the property name (the various enum values should be localized at point of display).
* Timeouts - we guard against the initial server request timing out via urllib, but should also keep track of the request closing, to stop a server stall keeping requests open. Need to check that
* server connection push-back - we should figure out a limit of concurrent connections the server wants to handle. Should be configurable via file
* we should add some level of caching, as these pages won't update that often. Process should be - call in, check if there's cache, return if so, otherwise kick off a scrape.
* find a better way to register Connectors when written (now need to add new type in a different file, which is simple but could be forgotten)
* extend Accommodation Types to be a more generic list (currently just what's needed for AirBnB)

#### Production things to think about:
* Screen scraping is quite hard to picture as a key component of a successful business model - should probably just be used as a backup, favoring using a proper API (and probably revenue sharing of some kind :) )
* this design is predicated on running cheap instances in AWS Lambda or the like. Cost should be a major consideration in where this should run, as that approach will get very costly at scale (and something like re-writing in an Actor pattern in Java/Akka could work well for that)
* caching across multiple regions will be interesting to solve. Use cloud-based solutions that auto-spread across regions


#### Scaling considerations:
* python is probably not the best language at large scale, it might be better to move to an actor pattern for scalability of this sort of thing (Akka on the JVM, Erlang on the EVM)
* if many people will work on this, then working in a compiled language could be a consideration as that can help catch errors early.
