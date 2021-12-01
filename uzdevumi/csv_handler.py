from csv import DictReader

from .models import Visit


def read_and_decode_csv(file, encoding='utf-8'):

    decoded_file = file.read().decode(encoding).splitlines()
    return decoded_file


def create_visit_from_row(row):

    visit = Visit(
        visitor=row['visitor'],
        date_time=row['date_time'],
        reason=row['reason'],
    )

    visit.save()


def visits_csv_rows_to_db(file):

    csv_reader = DictReader(file)

    for row in csv_reader:
        create_visit_from_row(row)

