#---------------------------------------------------#
# By Thejesh GN <i@thejeshgn.com>
#
#---------------------------------------------------#
import csv
from BeautifulSoup import BeautifulSoup
# Read in ward data
ward_values = dict(csv.reader(open('ward.csv')))

# Load the SVG map
svg = open('bbmp-ward.svg', 'r').read()
# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
# Find counties
paths = soup.findAll('path')

# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

# Color the counties based on unemployment rate
for p in paths:
	try:
	     ward_value =  ward_values[p['id']]
	     color = colors[int(ward_value)]
	     p['fill'] = color
	     #print p['id']		
	except:
	    continue
# Output map
print soup.prettify()
