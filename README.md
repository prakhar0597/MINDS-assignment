# Web-scrapping

This task was done as a part of a bigger Web Scraping project. Scraping data about Orbital launches from Wikipedia, the number of orbital launches every day based on a given constraint the output was to be given as a CSV file.

Data source: https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches

More about the problem: The number of orbital launches in the 'Orbital launches' table in Wikipedia Orbital Launches if at least one of its payloads is reported as 'Successful', 'Operational', or 'En Route'. For each launch, listed by date, the first line is the launch vehicle and any lines below it correspond to the payloads, of which there could be more than one. Please note that there might be multiple launches on a single day with multiple payloads within a single launch (we are only interested in the number of distinct launches).

Output format:__
date, value__
2019-01-01T00:00:00+00:00, 0__
2019-01-02T00:00:00+00:00, 1__
2019-01-03T00:00:00+00:00, 2__
2019-01-04T00:00:00+00:00, 3__
2019-01-05T00:00:00+00:00, 2__
...__
2019-12-31T00:00:00+00:00, 1
