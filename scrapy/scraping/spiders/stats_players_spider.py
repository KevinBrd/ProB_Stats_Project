import scrapy
from scrapy import Selector


class ProBStatsToScrape(scrapy.Spider):
    name = 'proBStats'
    start_urls = [
        "https://www.lnb.fr/pro-b/stats-engine/?option=player&season=2022&competition=265&type=total"
    ]

    def parse(self, response):
        temp = response.xpath('//tr[@class="odd" or @class="even"]/td').getall()
        size = 27
        res = [temp[idx: idx + size] for idx in range(0, len(temp), size)]
        for player in res:
            yield {
                'playerPicture': Selector(text=player[0]).xpath('//td/div/a/div/img/@src').get(),
                'playerName': Selector(text=player[0]).xpath('//td/div/a/div[@class="player-name"]/a/span[@class="first-name"]/text()').get()
                + Selector(text=player[0]).xpath('//td/div/a/div[@class="player-name"]/a/span[@class="last-name"]/text()').get(),
                'playerId': Selector(text=player[0]).xpath('//td/div/a/@href').get().lstrip('https://www.lnb.fr/pro-b/joueur?id='),
                'teamPicture': Selector(text=player[1]).xpath('//td/a/img/@src').get(),
                'teamName': Selector(text=player[1]).xpath('//td/a/span/text()').get(),
                'gamesPlayed': int(Selector(text=player[2]).xpath('//td/text()').get()),
                'gamesWhereStarted': int(Selector(text=player[3]).xpath('//td/text()').get()),
                'totalMinutes': int(Selector(text=player[4]).xpath('//td/text()').get()),
                'totalPoints': int(Selector(text=player[5]).xpath('//td/text()').get()),
                'totalFieldGoalAttempted': int(Selector(text=player[7]).xpath('//td/text()').get()),
                'totalFieldGoal': int(Selector(text=player[6]).xpath('//td/text()').get()),
                'totalFieldGoalPercentage': float(Selector(text=player[8]).xpath('//td/text()').get()),
                'totalThreePointAttempted': int(Selector(text=player[10]).xpath('//td/text()').get()),
                'totalThreePoint': int(Selector(text=player[9]).xpath('//td/text()').get()),
                'totalThreePointPercentage': float(Selector(text=player[11]).xpath('//td/text()').get()),
                'totalFreeThrowsAttempted': int(Selector(text=player[13]).xpath('//td/text()').get()),
                'totalFreeThrows': int(Selector(text=player[12]).xpath('//td/text()').get()),
                'totalFreeThrowsPercentage': float(Selector(text=player[14]).xpath('//td/text()').get()),
                'totalOffensiveRebounds': int(Selector(text=player[15]).xpath('//td/text()').get()),
                'totalDefensiveRebounds': int(Selector(text=player[16]).xpath('//td/text()').get()),
                'totalRebounds': int(Selector(text=player[17]).xpath('//td/text()').get()),
                'totalAssists': int(Selector(text=player[18]).xpath('//td/text()').get()),
                'totalBlockMade': int(Selector(text=player[19]).xpath('//td/text()').get()),
                'totalBlockSudden': int(Selector(text=player[20]).xpath('//td/text()').get()),
                'totalSteal': int(Selector(text=player[21]).xpath('//td/text()').get()),
                'totalTurnovers': int(Selector(text=player[22]).xpath('//td/text()').get()),
                'totalFoulsMade': int(Selector(text=player[23]).xpath('//td/text()').get()),
                'totalFoulsSudden': int(Selector(text=player[24]).xpath('//td/text()').get()),
                '+/-': int(Selector(text=player[25]).xpath('//td/text()').get()),
                'totalEvaluation': int(Selector(text=player[26]).xpath('//td/text()').get())
            }

# scrapy crawl proBStats -O dataset_proBstats.json