import scrapy


class PlayerInformationToScrape(scrapy.Spider):
    name = 'playersInformation'
    start_urls = [
        "https://www.lnb.fr/pro-b/stats-engine/?option=player&season=2022&competition=265&type=total"
    ]

    def parse(self, response):
        players_page_links = response.xpath('//tr[@class="odd" or @class="even"]/td/div/a/@href')
        yield from response.follow_all(players_page_links, self.parse_player)

    def parse_player(self, response):
        yield {
            'playerId': response.xpath('//main/div/div[@class="custom-container"]/div/@element_id').get(),
            'playerAge': int(response.xpath(
                '//main/div/div/div/div[@class="player-info desktop"]/div[@class="player-birthday"]/text()').get().split(
                "(")[1].split()[0]),
            'height (cm)': int(response.xpath(
                '//main/div/div/div/div[@class="player-info desktop"]/div[@class="player-height"]/text()').get().lstrip(
                'Taille : ').rstrip(' cm')),
            'playerRole': response.xpath(
                '//main/div/div/div/div[@class="player-info desktop"]/div[@class="player-role"]/text()').get().lstrip(
                '  Poste : ').rstrip(),
        }

# scrapy crawl playersInformation -O dataset_proBPlayers.json
