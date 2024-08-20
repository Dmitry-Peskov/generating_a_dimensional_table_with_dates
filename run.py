from collections import namedtuple
from datetime import datetime, timedelta
from typing import Optional


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
DateMetaData = namedtuple(typename="DateMetaData", field_names=FIELDS_LIST)

def get_next_day(date: datetime) -> datetime:
    return date + timedelta(days=1)


def get_month_name_ru(month_num: int) -> Optional[str]:
    months = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
    }
    return months.get(month_num, None)



def extract_metadata_from_date(date: datetime) -> DateMetaData:
    return DateMetaData(
        datetime=date,
        date=date.date(),
        year=date.year,
        month=date.month,
        month_name_ru=get_month_name_ru(month_num=date.month),
        month_name_en=date.strftime("%B"),
        day=date.day,
        week_num=date.isocalendar().week,
        week_day=date.weekday() + 1,
        quarter=(date.month - 1) // 3 + 1,
        is_weekends=1 if (date.weekday() + 1) in (6, 7) else 0
    )


def add_data_to_storage(date_metadata: DateMetaData, storage: list[dict]) -> None:
    storage.append(date_metadata._asdict())


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
