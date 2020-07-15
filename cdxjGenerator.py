# cdxj TimeMap generator
#
# This is script to generate dummy CDXJ data for testing other tools.
# A sample of the expected output style is appended to this code.
#
# Run it with $ python3 cdxjGenerator.py [numberOfLines]

import datetime
from faker import Faker
import random
import string
import surt
import sys
from tlds import tld_set


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def date_generator():
    fake = Faker()
    start_date = datetime.date(year=1, month=1, day=1)
    end_date = datetime.date(year=9999, month=12, day=31)
    dt = fake.date_time_between_dates(
        datetime_start=start_date, datetime_end=end_date)
    return dt.strftime('%Y%m%d%H%M%S')


def line_generator(provided_urir=None):
    while True:
        urir = provided_urir
        surted_urir = None
        if provided_urir is None:
            tld = random.sample(tld_set, 1)[0]
            host = id_generator(random.randrange(25))
            urir = f"{host}.{tld}"
            surted_urir = f"{tld},{host}/"
        else:
            surted_urir = surt.surt(
                provided_urir,
                path_strip_trailing_slash_unless_empty=True)

        date14 = date_generator()
        ipfs_char_range = string.ascii_letters + string.digits

        locators = (f"urn:ipfs/{id_generator(46, ipfs_char_range)}/"
                    f"{id_generator(46, ipfs_char_range)}")

        cdxj_line = (f"{surted_urir} {date14} "
                     "{"
                     f'"locator": "{locators}", '
                     f'"original_uri": "http://{urir}", '
                     '"mime_type": "text/html", "status_code": "200"}'
                     )

        yield cdxj_line


header_line = '!context ["http://tools.ietf.org/html/rfc7089"]'
print(header_line)


if len(sys.argv) <= 1:
    line_count = 10
else:
    line_count = int(sys.argv[1])

provided_urir = None
if len(sys.argv) == 3:
    provided_urir = sys.argv[2]

line_generator = line_generator(provided_urir)
while line_count > 0:
    print(next(line_generator))
    line_count -= 1

'''Sample CDXJ TimeMap pulled and generated from github.com/oduwsdl/ipwb

!context ["http://tools.ietf.org/html/rfc7089"]
!meta {"created_at": "2019-02-06T19:01:10.273792", "generator": "InterPlanetary Wayback v.0.2018.10.15.1346"}
us,anothersite)/ 20161231110000 {"locator": "urn:ipfs/QmNQX5gEjbEPModBHXb6w4EWveLkZ57uEC9Kzh8bho7QmL/QmdGwKcB1JVttQ419yjqFN1WdQbJ9V2PSdfLKGXMdoUivg", "original_uri": "http://anothersite.us/", "mime_type": "text/html", "status_code": "200"}
us,memento)/ 20130202100000 {"locator": "urn:ipfs/QmNQX5gEjbEPModBHXb6w4EWveLkZ57uEC9Kzh8bho7QmL/Qmf7YmS73j36H33w2zYujUn3atQBK1VLiL51cwCrvVKkBC", "original_uri": "http://memento.us/", "mime_type": "text/html", "status_code": "200"}
us,memento)/ 20140114100000 {"locator": "urn:ipfs/QmNQX5gEjbEPModBHXb6w4EWveLkZ57uEC9Kzh8bho7QmL/QmZtSHMxX9roQPHLvRyPkrR7azqfj5cmpYa5sFQkZfkLXf", "original_uri": "http://memento.us/", "mime_type": "text/html", "status_code": "200"}
us,memento)/ 20140115101500 {"locator": "urn:ipfs/QmNQX5gEjbEPModBHXb6w4EWveLkZ57uEC9Kzh8bho7QmL/QmXDsUhfSzvtTwakyt6McXnjpzAw2BQvAcVdSCWSp2Tfge", "original_uri": "http://memento.us/", "mime_type": "text/html", "status_code": "200"}
us,memento)/ 20161231110000 {"locator": "urn:ipfs/QmNQX5gEjbEPModBHXb6w4EWveLkZ57uEC9Kzh8bho7QmL/QmVGSLKM2oQQZfoUnuBYqNzi4Cy2FiAgdG6pdpBpuBKS1N", "original_uri": "http://memento.us/", "mime_type": "text/html", "status_code": "200"}
us,memento)/ 20161231110001 {"locator": "urn:ipfs/QmNQX5gEjbEPModBHXb6w4EWveLkZ57uEC9Kzh8bho7QmL/QmaJ6aBdMrZPiJHPqWbzqVuxiWBScv37JvAhiHAbCzgsF1", "original_uri": "http://memento.us/", "mime_type": "text/html", "status_code": "200"}
us,someotheruri)/ 20161231110000 {"locator": "urn:ipfs/QmNQX5gEjbEPModBHXb6w4EWveLkZ57uEC9Kzh8bho7QmL/QmdxGXvLVFiUy7gLwww5TUTgkWdrAEaNmhgEc4bcUpGBke", "original_uri": "http://someotherURI.us/", "mime_type": "text/html", "status_code": "200"}
'''  # noqa: D301
