# Генерация размерной таблицы с датами | Generating a dimensional table with dates


Данный скрипт предназначен для генерации размерной таблицы с датами для произвольного диапазона (включая обе границы).  
Скрипт использует стандартный инструментарий Python и не требует установки сторонних пакетов.  
Разработанно и протестированно на  **[Python 3.10.4](https://www.python.org/downloads/release/python-3104/)**  
Диапазон задается через переменные **start_date** и **end_date** в блоке:  
```python
if __name__ == "__main__":
    start_date: datetime = datetime(year=2000, month=1, day=1)  # начало диапазона дат
    end_date: datetime = datetime(year=2050, month=1, day=1)    # окончание диапазона дат
    ...
```
В процессе работы скрипт для каждой даты, входящей в диапазон, формирует информацию вида:   

| datetime          |date| year |month|month_name_ru|month_name_en|day|week_num|week_day| quarter | is_weekends |
|-------------------|-|---|-|-|-|-|-|-|-|------------|
| 2000-01-01 00:00:00 |2000-01-01|2000|1|Январь|January|1|52|6|1|1|
|...|...|...|...|...|...|...|...|...|...|...|

Где:  

|Столбец| Пояснение                                                                    |
|-|------------------------------------------------------------------------------|
|datetime| Дата в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС                                           |
|date| Дата в формате ГГГГ-ММ-ДД                                                    |
|year| Год ГГГГ                                                                     |
|month| Месяц (число 1 - 12)                                                         |
|month_name_ru| Рускоязычное название месяца                                                 |
|month_name_en| Англоязыное название месяца                                                  |
|day| День (число 1 - 31)                                                          |
|week_num| Номер недели в году (число)                                                  |
|week_day| Номер дня недели (число, 1 - ПН; 7 - ВС)                                     |
|quarter| Номер квартала (число, 1 - 4)                                                |
|is_weekends| Флаг, говорящий является ли дата субботой или воскресеньем (1 - да; 0 - нет) |

Опираясь на заданные в **start_date** и **end_date** значения, формируется название будущих выходных файлов.  
Названия формируются по маскам:  
- _dimensional_table_with_dates_ДД.ММ.ГГГГ-ДД.ММ.ГГГГ.csv_
- _dimensional_table_with_dates_ДД.ММ.ГГГГ-ДД.ММ.ГГГГ.json_

Результат записывается в соответствующие файлы в формате:  
Для **csv**:
```csv
datetime,date,year,month,month_name_ru,month_name_en,day,week_num,week_day,quarter,is_weekends
2000-01-01 00:00:00,2000-01-01,2000,1,Январь,January,1,52,6,1,1
2000-01-02 00:00:00,2000-01-02,2000,1,Январь,January,2,52,7,1,1
2000-01-03 00:00:00,2000-01-03,2000,1,Январь,January,3,1,1,1,0
```
Для **json**:
```json
[
  {
    "datetime": "2000-01-01 00:00:00",
    "date": "2000-01-01",
    "year": 2000,
    "month": 1,
    "month_name_ru": "\u042f\u043d\u0432\u0430\u0440\u044c",
    "month_name_en": "January",
    "day": 1,
    "week_num": 52,
    "week_day": 6,
    "quarter": 1,
    "is_weekends": 1
  },
  {
    "datetime": "2000-01-02 00:00:00",
    "date": "2000-01-02",
    "year": 2000,
    "month": 1,
    "month_name_ru": "\u042f\u043d\u0432\u0430\u0440\u044c",
    "month_name_en": "January",
    "day": 2,
    "week_num": 52,
    "week_day": 7,
    "quarter": 1,
    "is_weekends": 1
  },
]
```

#### Пример сгенерированных скриптом данных для диапазона 1.01.2000 - 1.01.2050:

- [dimensional_table_with_dates_01.01.2000-01.01.2050.csv](https://github.com/Dmitry-Peskov/generating_a_dimensional_table_with_dates/blob/main/dimensional_table_with_dates_01.01.2000-01.01.2050.csv)
- [dimensional_table_with_dates_01.01.2000-01.01.2050.json](https://github.com/Dmitry-Peskov/generating_a_dimensional_table_with_dates/blob/main/dimensional_table_with_dates_01.01.2000-01.01.2050.json)
