import csv
import json
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
DateMetaData = namedtuple(typename="DateMetaData", field_names=FIELDS_LIST) # контейнер, для хранения метаданных конкретной даты

def get_next_day(date: datetime) -> datetime:
    """Получить следующий за переданным в аргументы день"""
    return date + timedelta(days=1)


def get_month_name_ru(month_num: int) -> Optional[str]:
    """На основе номера месяца, получить его русскоязычное наименование"""
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
    """Извлечь из конкретной даты её метаданные"""
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
    """Перевести метаданные даты в словарь (dict) и добавить в промежуточное хранилище"""
    storage.append(date_metadata._asdict())


def generate_filename(start: datetime, end: datetime) -> str:
    """Сгенерировать название файла по маске: dimensional_table_with_dates_ДД.ММ.ГГГГ-ДД.ММ.ГГГГ"""
    return f"dimensional_table_with_dates_{start.strftime('%d.%m.%Y')}-{end.strftime('%d.%m.%Y')}"


def write_to_csv(filename: str, fields_name: list[str], data: list[dict]) -> None:
    """Записать результат в csv файл"""
    with open(f"{filename}.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields_name)
        writer.writeheader()
        writer.writerows(data)


def write_to_json(filename: str, data: list[dict]) -> None:
    """Записать результат в json файл"""
    with open(f"{filename}.json", "w", encoding="utf-8") as file:
        json_data = json.dumps(data, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2)
        file.write(json_data)


if __name__ == "__main__":
    start_date: datetime = datetime(year=2000, month=1, day=1)  # начало диапазона дат
    end_date: datetime = datetime(year=2050, month=1, day=1)    # окончание диапазона дат
    result_list: list[dict] = []                                # список для промежуточного хранения результирующей последовательности дат
    current_processed_date: datetime = start_date               # текущая дата из которой извлекаются метаданные и сохраняются в промежуточный результат
    # в цикле перебираем каждую дату из заданного диапазона, сохраняем метаданные каждой в result_list, до тех пор пока не превысим end_date
    while current_processed_date < end_date:
        metadata: DateMetaData = extract_metadata_from_date(date=current_processed_date)  # извлекаем метаданные из даты в current_processed_date
        add_data_to_storage(date_metadata=metadata, storage=result_list)                  # сохраняем метаданные в result_list
        current_processed_date:datetime = get_next_day(date=current_processed_date)       # переключаемся на следующую дату
    file_name: str = generate_filename(start=start_date, end=end_date)                    # генерируем название файла по шаблону
    write_to_csv(filename=file_name, fields_name=FIELDS_LIST, data=result_list)  # записываем результат в csv файл
    write_to_json(filename=file_name, data=result_list)                          # записываем результат в json файл
