## Практика 1. Docker. Сокеты. Сериализация и десериализация данных

**Приложение для тестирования различных форматов сериализации.**

Вариант с прокси-сервисом - несколько отдельных контейнеров на Python тестируют различные форматы сериализации. Входящие запросы обрабатываются прокси-сервисом с портом UDP 2000, который переадресует запрос нужному контейнеру и возвращает результат.

Запрос: get_result {название формата}. Возможные форматы: 'native', 'xml', 'json', 'protobuf', 'yaml', 'msgpack', 'avro'.

Запуск контейнеров:

```
docker compose build
docker compose up -d
```

Пример работы с контейнерами с помощью netcat:

```
nc -u 127.0.0.1 2000
get_result native
native - 373 - 4.79μs - 5.16μs
get_result xml
xml - 1071 - 289.1μs - 311.82μs
get_result json
json - 406 - 19.33μs - 8.54μs
get_result protobuf
protobuf - 235 - 135.0μs - 78.79μs
get_result yaml
yaml - 359 - 1214.33μs - 2108.72μs
get_result msgpack
msgpack - 300 - 4.57μs - 5.13μs
get_result avro
avro - 213 - 224.4μs - 159.72μs
```

Для тестирования используется следующая структура данных:

```
test_dict = {"int": 1001,
             "float": 7.77,
             "string": "String!",
             "array_int": [115, 20897, -33],
             "array_float": [-1.9, 1500.567, 3.5],
             "array_string": ["red", "orange", "yellow"],
             "dict_int": {"one": 115, "two": 20897, "three": -33},
             "dict_float": {"good": -1.9, "okay": 1500.567, "bad": 3.5},
             "dict_string": {"strawberry": "red", "tangerin": "orange", "lemon": "yellow"},
             }
```

Вывод программы для заданных форматов:

* проверяется корректность их работы (что словарь, полученный после сериализации и десериализации, равен исходному),
* находится размер сериализованного объекта в байтах,
* измеряется среднее время из 1000 запусков сериализации и десериализации в микросекундах.

Пример:

```
native - 373 - 3.07μs - 4.64μs
```
