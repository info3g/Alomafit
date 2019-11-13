import re
from urllib.request import urlopen

from bs4 import BeautifulSoup


#################################################

def remove_empty_lines1(text):
    return "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()])


# removing empty lines from text, gather the resulted text with space between each phrase
def remove_empty_lines2(text):
    text1 = " ".join([ll.rstrip() for ll in text.splitlines() if ll.strip()])
    text2 = " ".join(text1.split())
    return text2


################################################
class Product:

    def __init__(self, url, sizes, parts, unit):
        self.url = url
        self.parts = parts
        self.unit = unit
        self.sizes = sizes


#################################################
class measure:

    def __init__(self, part, measurements):
        self.measurements = measurements
        self.part = part


################################################
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))


##################################################

# Extract product info from url...

def extractTable(url, ok):
    allTables = []
    # get response from product url
    page = url
    if (ok):
        page = urlopen(url)

        # get html tags from response
    soup = BeautifulSoup(page, 'html.parser')
    # get the body only from whole htnl page
    try:
        body = soup.find('body')

        # finally get the tables only from the body after cleaning all unnecessary tags

        tables = [x for x in body.findAll('table') if (
            any(M in x.get_text().lower() for M in ['bust', 'hip', 'chest', 'seat', 'shoulder', 'width', 'waist']))]

        for table in tables:
            table_header = []
            imag = False
            if table.find('thead'):
                table_header = [x.get_text().lower() for x in table.find('thead').findAll('td')]
            else:
                table_header = [x.get_text().lower() for x in table.find('tbody').findAll('tr')[0].findAll('td')]
            if ((table.find('tbody').findAll('tr')[0].find('img'))):
                imag = True

            if (
                    any(M in " ".join(table_header) for M in
                        ['bust', 'hip', 'chest', 'seat', 'width', 'waist', 'shoulder'])):

                parts = []
                sizes = []

                for temp in table_header:
                    if (any(M in temp for M in ['bust', 'hip', 'chest', 'seat', 'width', 'waist', 'shoulder'])):
                        measurements = []

                        for tr in table.find('tbody').findAll('tr')[1:]:
                            if (tr.findAll('td')):
                                if (imag):
                                    measurements.append(tr.findAll('td')[table_header.index(temp) - 1].get_text())

                                else:
                                    measurements.append(tr.findAll('td')[table_header.index(temp)].get_text())

                        parts.append(measure(temp, measurements))
                for tr in table.find('tbody').findAll('tr')[1:]:
                    sizes.append(remove_empty_lines1(tr.findAll('td')[0].get_text()))
                allTables.append(Product(url, sizes, parts, 'in'))
            elif (len(table_header) > 1):
                parts = []

                for tr in table.find('tbody').findAll('tr'):
                    part = ''
                    measurements = []
                    if (tr.find('th')):
                        part = tr.find('th').get_text()
                        measurements = [y.get_text() for y in tr.findAll('td')]
                    else:
                        part = tr.findAll('td')[0].get_text()

                        measurements = [y.get_text() for y in tr.findAll('td')[1:]]

                    if (any(M in part.lower() for M in ['bust', 'hip', 'chest', 'seat', 'width', 'waist', 'shoulder'])):
                        parts.append(measure(part, measurements))

                allTables.append(Product(url, table_header, parts, 'in'))

            else:

                parts = []
                sizes = ['small', 'medium', 'large', 'x-large', 'x-small', 's ', 'xxs ', 'xs ', 'm ', 'l ', 'xl ',
                         'xxl ', '1x ', '2x ', '3x ' \
                    , '4x ', 's:', 'm:', 'l:', 'xl:', 'xxl:', 'xxxl:', 'xxs', 'xs', 'm', 'l', 'xl', 'xxl', '1x',
                         '2x', '3x', 's' \
                    , '4x', 'size 1', 'size 2', 'size 3', 'size 4', 'size 6', 'size 7', 'size 5', 'size 8']
                part = [p for p in ['bust', 'hip', 'chest', 'seat', 'width', 'waist', 'shoulder'] if
                        p in table.get_text().lower()]

                for p in part:
                    row = [tr for tr in table.findAll('tr') if p in tr.get_text().lower()][0]
                    if (row.findAll('td')):
                        indexs = [ele.get_text().lower() for ele in row.findAll('td')]
                    elif (row.findAll('th')):
                        indexs = [ele.get_text().lower() for ele in row.findAll('th')]

                    ind = 0
                    index = False
                    while ind < len(indexs):
                        if p in indexs[ind]:
                            index = ind
                        ind = ind + 1
                    rows = [tr for tr in table.findAll('tr') if tr != '\n']

                    column = []
                    for r in rows:
                        if (len(r.findAll('td')) > index and (not p in r.get_text().lower())):
                            column.append(r.findAll('td')[index].get_text().lower())
                        elif (len(r.findAll('th')) > index and (not p in r.get_text().lower())):
                            column.append(r.findAll('th')[index].get_text().lower())

                    row_measure = [M.get_text().lower() for M in row.findAll('td') if hasNumbers(M.get_text())]
                    column_measure = [M for M in column if hasNumbers(M)]

                    if (len(column_measure) >= len(row_measure)):
                        parts.append(measure(p, column_measure))
                    else:
                        parts.append(measure(p, row_measure))

                    table_header = []
                    for row in rows:
                        for si in row.findAll('td'):

                            if si.get_text().lower() in sizes:
                                table_header.append(si.get_text().lower())

                    allTables.append(Product(url, table_header, parts, 'in'))

        if (len(allTables) >= 1):
            return allTables[0]
        else:
            return False
    except:
        return False


##########################################################

def bust_check(text):
    part = re.compile(r'bust[\s]?[,|:|//]?[\s]?([0-9]+)')
    if (part.search(text)):
        return part.search(text.lower()).group()
    else:
        return False


def waist_check(text):
    part = re.compile(r'waist[\s]?[,|:|//]?[\s]?([0-9]+)')
    if (part.search(text)):
        return part.search(text.lower()).group()
    else:
        return False


def hip_check(text):
    part = re.compile(r'hip[\s]?[,|:|//]?[\s]?([0-9]+)')
    if (part.search(text)):
        return part.search(text.lower()).group()
    else:
        return False


def width_check(text):
    part = re.compile(r'width[\s]?[,|:|//]?[\s]?([0-9]+)')
    if (part.search(text)):
        return part.search(text.lower()).group()
    else:
        return False


def shoulder_check(text):
    part = re.compile(r'shoulder[\s]?[,|:|//]?[\s]?([0-9]+)')
    if (part.search(text)):
        return part.search(text.lower()).group()
    else:
        return False


def seat_check(text):
    part = re.compile(r'seat[\s]?[,|:|//]?[\s]?([0-9]+)')
    if (part.search(text)):
        return part.search(text.lower()).group()
    else:
        return False


def size_check(text):
    sizes = ['small', 'medium', 'large', 'x-large', 'x-small', 'xxs ', 'xs ', 'm ', 'l ', 'xl ', 'xxl ', '1x ', '2x ',
             '3x ', '4x ', 's:', 'm:', \
             'l:', 'xl:', 'xxl:', 'xxxl:', 'size 1', 'size 2', 'size 3', 'size 4', 'size 6', 'size 7', 'size 5',
             'size 8']
    size = re.compile(r'small|medium|large|x-large|x-small|xl:|xxl:|xxxl:|s:|m:|\
           l:|xxs |xs |s |m |xl |xxl |l |1x |2x |3x |4x|size 1|size 2|size 3|size 4|size 6|size 7|size 5|size 8')

    if (any(M in text.lower() for M in sizes)):

        if (bust_check(text.lower()) or waist_check(text.lower()) or hip_check(text.lower()) or width_check(
                text.lower()) \
                or seat_check(text.lower()) or shoulder_check(text.lower())):
            if size.search(text.lower()):
                return size.search(text.lower()).group()
            else:
                return False
        else:
            return False


################################################################


def extractText(url, ok):
    # get response from product url
    page = url
    if (ok):
        page = urlopen(url)
        # get html tags from response
    soup = BeautifulSoup(page, 'html.parser')
    # get the body only from whole htnl page
    try:
        body = soup.find('body')
        # remove all scripts from body if it has any..
        [body.script.decompose() for x in body.findAll('script')]
        # remove footer if there is
        [body.footer.decompose() for x in body.findAll('footer')]
        # remove images from the body if it has any..
        [body.img.decompose() for x in body.findAll('img')]
        [body.style.decompose() for x in body.findAll('style')]
        # remove nav if there is
        [body.nav.decompose() for x in body.findAll('nav')]
        [body.noscript.decompose() for x in body.findAll('noscript')]
        [body.form.decompose() for x in body.findAll('form')]
        # finally get the text only from the body after cleaning all unnecessary tags
        text = remove_empty_lines1(body.get_text()).lower()
        return text
    except:
        return False


###############################################################################


def extract_table_from_text(url, ok):
    try:
        lines = extractText(url, ok).lower()

        sizes = []
        busts = []
        waists = []
        shoulders = []
        hips = []

        seats = []
        width = []

        for line in lines.split('\n'):
            line = line.replace("\"", "").lower()

            if (size_check(line)):
                sizes.append(size_check(line))

            if (bust_check(line)):
                busts.append(bust_check(line))
            if (waist_check(line)):
                waists.append(waist_check(line))
            if (hip_check(line)):
                hips.append(hip_check(line))
            if (shoulder_check(line)):
                shoulders.append(shoulder_check(line))
            if (seat_check(line)):
                seats.append(seat_check(line))
            if (width_check(line)):
                width.append(width_check(line))
        if (len(sizes) == 1):
            sizes = ['onesize']
        if (len(busts) >= 1 or len(hips) >= 1 or len(waists) >= 1 or len(shoulders) >= 1 or len(seats) >= 1 or (
                len(width) >= 1)):
            return sizes, busts, hips, waists, width, shoulders, seats
        else:
            return False
    except:
        return False


##########################################################

def extractLinks(url):
    # get response from product url
    page = urlopen(url)
    # get html tags from response
    soup = BeautifulSoup(page, 'html.parser')
    # get the body only from whole htnl page
    try:
        body = soup.find('body')
        # remove all scripts from body if it has any..
        [body.script.decompose() for x in body.findAll('script')]
        # remove footer if there is
        [body.footer.decompose() for x in body.findAll('footer')]
        # remove images from the body if it has any..
        [body.img.decompose() for x in body.findAll('img')]
        [body.style.decompose() for x in body.findAll('style')]
        # remove nav if there is
        [body.nav.decompose() for x in body.findAll('nav')]
        # finally get the links text only for each link after cleaning all unnecessary tags
        links_url = [x for x in body.findAll('a') if
                     (any(M in remove_empty_lines2(x.get_text()).lower() for M in ['size', \
                                                                                   'sizing', 'fit', 'fitting',
                                                                                   'measurements']))]
        if (len(links_url) > 1):
            return links_url
        else:
            return False
    except:
        return False


###################################################################


#################################################################

def get_meauserments(url):
    valid = re.compile(r'([0-9]+)')
    unit = re.compile(r'([cm|centimeter])')
    partre = re.compile(r'(bust|hip|chest|seat|width|waist|shoulder)')
    result = extractTable(url, True)
    if (result):

        table = result

        for y in table.parts:
            if (unit.search(y.measurements[0]) or unit.search(y.part)):
                table.unit = "cm"

            y.measurements = [valid.search(M.lower()).group() for M in y.measurements]
            y.part = partre.search(y.part).group()
        return table

    elif (extract_table_from_text(url, True)):

        s, b, h, w, width, sh, seats = extract_table_from_text(url, True)
        iunit = "in"

        parts = []
        if (len(b)):
            if (unit.search(b[0])):
                iunit = "cm"

            b = [re.sub("\D", "", M) for M in b]
            parts.append(measure('bust', b))
        if (len(h)):
            if (unit.search(h[0])):
                iunit = "cm"
            h = [re.sub("\D", "", M) for M in h]
            parts.append(measure('hip', h))
        if (len(w)):
            if (unit.search(w[0])):
                iunit = "cm"
            w = [re.sub("\D", "", M) for M in w]
            parts.append(measure('waist', w))
        if (len(width)):
            if (unit.search(width[0])):
                iunit = "cm"
            width = [re.sub("\D", "", M) for M in width]
            parts.append(measure('width', width))
        if (len(sh)):
            if (unit.search(sh[0])):
                iunit = "cm"
            sh = [re.sub("\D", "", M) for M in sh]
            parts.append(measure('shoulder', sh))
        if (len(seats)):
            if (unit.search(seats[0])):
                iunit = "cm"
            seats = [re.sub("\D", "", M) for M in seats]
            parts.append(measure('seats', seats))

        return (Product(url, s, parts, iunit))

    return False

# #############################################################
# ###example1
# x = get_meauserments("https://www.purecycles.com/collections/clothing/products/pure-fix-1940s-tee")
# if (x):
#     for y in x.parts:
#         print(y.part)
#         print(y.measurements)
#     print(x.sizes)
#
# ####################################################################
# ###example2
# x = get_meauserments("https://shopdressup.com/brianna-acid-wash-tie-front-top/")
# if (x):
#     for y in x.parts:
#         print(y.part)
#         print(y.measurements)
#     print(x.sizes)
#
# ######################################################################
# # example3 needs selenium so return false
# x = get_meauserments(
#     "https://www.taylorstitch.com/collections/mens-outerwear/products/the-moto-jacket-in-midnight-steerhide")
# if (x):
#     for y in x.parts:
#         print(y.part)
#         print(y.measurements)
#     print(x.sizes)
