""">> SCRAPER.PY
This scraper politely scrapes restaurant information from the Michelin Guide's
website.
It assumes the user has checked what the value for `target_url_location` is
to complete https://guide.michelin.com/gb/en/{target_url_location}/restaurants.
"""

# Libraries
import logging
from pathlib import Path
import requests
import random

# Setting up scraper's logger - important to keep info-level logs as the Michelin
# guide restaurant tends to open pop-ups after hitting a page viewing quota.
# Monitoring if breaks/interruptions occur is important.
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='scraper.log',
    filemode='a',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding='utf-8'
)

# Custom resources
# cwd = Path(__file__).resolve().parent
# scrapertools = cwd.parent / 'src' / 'scrapertools.py'

from src.scrapertools import HEADERS


class Scraper:
    def __init__(
        self,
        target_url_location: str
    ):
        # Initialising logger and setting key variables
        self.logger = logging.getLogger(__name__)
        self.url_location = target_url_location
        self.url = "https://guide.michelin.com/"
        self.target_url = f"gb/en/{target_url_location}/restaurants"

        # Start session with a base header - it'll be shuffled as we go
        self.session = requests.Session()
        self.session.headers = ({'User-Agent': random.shuffle(HEADERS)})

        # Set a starting header - DONE
        # Get robots.txt delay and checker if I can visit the page
        # Capture delay
        # Reshuffle the header, set page referrer as homepage and grab the total results + results per page
        # Divide results per page by total results to calculate total iterations
        # while ... collect the data per page
            # Each page requires opening a new one and grabbing its data
            # From each page, capture the following:
                # restaurant name
                # address
                # price range
                # cuisine
            # Append results/store them somewhere readable
            # Move on to the next page
            # Reshuffle header
            # Rinse, repeat

if __name__ == "__main__":
    Scraper('selection/singapore')