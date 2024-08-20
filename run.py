from collections import namedtuple
from datetime import datetime, timedelta


FIELDS_LIST: list[str] = [
    "datetime",       # 2024-08-20 00:00:00
    "date",           # 2024-08-20
    "year",           # 2024
    "month",          # 8
    "month_name_ru",  # август
    "month_name_en",  # august
    "day",            # 20
    "week_num",       # 34
    "week_day",       # 2
    "quarter",        # 3
    "is_weekends"     # 0
]
FIELDS_STR = ", ".join(FIELDS_LIST) # "datetime, date, year, month, month_name_ru, month_name_en, day, week_num, week_day, quarter, is_weekends"
DateMetaData = namedtuple(typename="DateMetaData", field_names=FIELDS_STR)

def get_next_day(date: datetime) -> datetime:
    return date + timedelta(days=1)



def extract_metadata_from_date(date: datetime) -> DateMetaData:
    raise NotImplemented


def add_data_to_storage(date_metadata: DateMetaData, storage: list[dict]) -> None:
    raise NotImplemented


def generate_filename(start: datetime, end: datetime) -> str:
    raise NotImplemented


def write_to_csv(filename: str, data: list[dict]) -> None:
    raise NotImplemented


if __name__ == "__main__":
    start_date: datetime = datetime(year=2000, month=1, day=1)  # начало диапазона дат
    end_date: datetime = datetime(year=2100, month=1, day=1)    # окончание диапазона дат
    result_list: list[dict] = []                                # список для промежуточного хранения результирующей последовательности дат
    current_processed_date: datetime = start_date               # текущая дата из которой извлекаются метаданные и сохраняются в промежуточный результат
    # в цикле перебираем каждую дату из заданного диапазона, сохраняем метаданные каждой в result_list, до тех пор пока не превысим end_date
    while current_processed_date < end_date:
        metadata: DateMetaData = extract_metadata_from_date(date=current_processed_date)  # извлекаем метаданные из даты в current_processed_date
        add_data_to_storage(date_metadata=metadata, storage=result_list)                  # сохраняем метаданные в result_list
        current_processed_date:datetime = get_next_day(date=current_processed_date)       # переключаемся на следующую дату
    file_name: str = generate_filename(start=start_date, end=end_date)                    # генерируем название файла по шаблону
    write_to_csv(filename=file_name, data=result_list)  # записываем результат в csv файл
