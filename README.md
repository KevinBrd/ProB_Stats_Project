# ProB Players Stats analysis

This project scrapes data from the official website of the ProB to build a dataset of its players.
Afterwards, we correct the data, EDA and PCA.

Original website **https://www.lnb.fr/pro-b/stats-engine/?option=player&season=2022&competition=265&type=total**.

Author: Kévin Bourdon

## Dependencies

Python 3 (3.10 or higher)
Jupyter Notebook (6.4.7 or higher)
Scrapy (2.8.0 or higher)

Install these tools with

```shell
$ sudo apt install python3-pip
$ pip install notebook
$ pip install scrapy
```

## Setup the dataset

First, change directory to "/scrapy/scraping".
```shell
$ scrapy crawl proBStats -O dataset_proBstats.json
$ scrapy crawl playersInformation -O dataset_proBPlayers.json
$ python script_clean_duplicate_players.py
```

## Examples

Open "main.ipynb".

## Other information

This project is in public, but it is part of a larger project that scrapes the stats of players from multiple leagues to get better results if you want to scoot

## Contact

For questions or comments, please contact [Kévin Bourdon](mailto:kevin.bourdon.etu@univ-lille.fr). I would love
to hear from you.
