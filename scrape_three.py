
import json
from time import sleep
import urllib.request


def run_scrape_for_three_properties(host='127.0.0.1', port=8083):
    # this needs a running server to contact
    request = urllib.request.Request(
        data=json.dumps({"url": "https://www.airbnb.co.uk/rooms/14531512?s=51"}).encode('utf8'),
        url="http://{0}:{1}/accommodation".format(host, port)
    )
    request.add_header('Content-Type', 'application/json')

    requested_data = urllib.request.urlopen(
        request
    )
    data = requested_data.read()
    print(data)
    sleep(2)

    request = urllib.request.Request(
        data=json.dumps({"url": "https://www.airbnb.co.uk/rooms/19278160?s=51"}).encode('utf8'),
        url="http://{0}:{1}/accommodation".format(host, port)
    )
    request.add_header('Content-Type', 'application/json')

    requested_data = urllib.request.urlopen(
        request
    )
    data = requested_data.read()
    print(data)
    sleep(2)

    request = urllib.request.Request(
        data=json.dumps({"url": "https://www.airbnb.co.uk/rooms/16141909?s=51"}).encode('utf8'),
        url="http://{0}:{1}/accommodation".format(host, port)
    )
    request.add_header('Content-Type', 'application/json')

    requested_data = urllib.request.urlopen(
        request
    )
    data = requested_data.read()
    print(data)


if __name__ == "__main__":
    run_scrape_for_three_properties('127.0.0.1', 8083)
