import os
from datetime import datetime, timedelta

from nyct_gtfs import NYCTFeed


def main():
    feed = NYCTFeed("2", api_key=os.environ['API_KEY'])
    trips = feed.filter_trips(line_id=["2", "3"], travel_direction="N")
    print(trips[3])


if __name__ == '__main__':
    main()
