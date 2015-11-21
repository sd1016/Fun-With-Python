page = '<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Udacity</title></head><body><h1>Udacity</h1><p><b>Udacit' \
       'y</b> is a private institution of<a href="http://www.wikipedia.org/wiki/Higher_education">higher education found' \
       'ed by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike S' \
       'okolsky with the goal to provide university-level education that is "both high quality and low cost".</p>   <p> ' \
       'It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Uda' \
       'city is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="htt' \
       'p://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p>      </body></html>'

start = 0
start_index = page.find('<a href="', start)
while start_index != -1:
    end_index = page.find('">', start_index)
    print page[(start_index + len('<a href="')):end_index]
    start = end_index + 2
    start_index = page.find('<a href="', start)