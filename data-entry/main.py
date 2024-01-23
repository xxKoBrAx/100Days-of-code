from scaper import Scraper
from compiler import Compiler

scraper = Scraper()
compiler = Compiler()
for n in range(len(scraper.addresses - 1)):
    compiler.fill_form(scraper.addresses[n], scraper.prices[n], scraper.links[n])

