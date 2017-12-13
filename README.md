# Marvel Report

### Set up

##Requires Python 3.4

Add the Marvel API client secret key to the file `privateKey.txt` with no trailing whitespace

In the terminal, run `python marvel.py`

The first execution of the project will be slow as it will scrape the Marvel API for data. Subsequent runs will run quicker
because the API results are cached

To run the tests:

`python report_cache_test.py`

`python client_test.py`

`python report_printer_test.py`