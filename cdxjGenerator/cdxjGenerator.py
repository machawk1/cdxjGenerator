import datetime
from faker import Faker
import random
import string
import surt
import sys


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_line(provided_urir=None):
    fake = Faker()
    start_date = datetime.date(year=1, month=1, day=1)
    end_date = datetime.date(year=9999, month=12, day=31)
    ipfs_char_range = string.ascii_letters + string.digits
    while True:
        urir = provided_urir or fake.uri()

        surted_urir = surt.surt(
            urir,
            path_strip_trailing_slash_unless_empty=True)

        date14 = fake.date_time_between_dates(
            start_date, end_date).strftime('%Y%m%d%H%M%S')

        locators = (f"urn:ipfs/{id_generator(46, ipfs_char_range)}/"
                    f"{id_generator(46, ipfs_char_range)}")

        cdxj_line = (f"{surted_urir} {date14} "
                     "{"
                     f'"locator": "{locators}", '
                     f'"original_uri": "{urir}", '
                     '"mime_type": "text/html", "status_code": "200"}'
                     )

        yield cdxj_line


def main():
    header_line = '!context ["http://tools.ietf.org/html/rfc7089"]'
    print(header_line)

    if len(sys.argv) <= 1:
        line_count = 10
    else:
        line_count = int(sys.argv[1])

    provided_urir = None
    if len(sys.argv) == 3:
        provided_urir = sys.argv[2]

    line_generator = generate_line(provided_urir)
    while line_count > 0:
        print(next(line_generator))
        line_count -= 1


if __name__ == "__main__":
    main()
