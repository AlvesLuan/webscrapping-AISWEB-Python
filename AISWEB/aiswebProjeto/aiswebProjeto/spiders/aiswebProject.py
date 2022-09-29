import scrapy


class projetoAISWEBSpider(scrapy.Spider):
    name = 'aisweb'
    allowed_domains = ['aisweb.decea.mil.br']
#   start_urls = ['https://aisweb.decea.mil.br/?i=aerodromos&codigo=SBMT']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://aisweb.decea.mil.br/?i=aerodromos&codigo={self.text}']

    def parse(self, response):
        for blocotempo in response.css('.order-sm-12'):
            print('\n')
            yield {
                'nascerdosol': blocotempo.css('sunrise ::text').get(),
                'pordosol': blocotempo.css('sunset ::text').get()
            }

        for blocotaf in response.css('p:nth-child(14)'):
            print('\n')
            yield {
                'TAF': blocotaf.css('p:nth-child(14) ::text').get()
            }

        for blocometar in response.css('p:nth-child(12)'):
            print('\n')
            yield {
                'METAR': blocometar.css('p:nth-child(12) ::text').get()
            }

        for blococarta in response.css('.order-sm-12'):
            print('\n')
            yield {
                'cartasDisponiveis': blococarta.css('.list-icons-style-2 a ::text').getall()
            }

