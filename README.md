# distributed_config

Пример входящего JSON:
```json

{   "system_name" : "testik5",
    "value_names": [
      {"name":"22"},
      
      {"name":"15"}
    ]

}

```

Вывод (для тестирования):
```json

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "value_names": [
                {
                    "name": "22"
                },
                {
                    "name": "15"
                }
            ],
            "system_name": "testik5",
            "version": 1,
            "in_use_indicator": "inactive"
        },
        {
            "value_names": [
                {
                    "name": "22"
                },
                {
                    "name": "15"
                }
            ],
            "system_name": "testik5",
            "version": 2,
            "in_use_indicator": "inactive"
        },
        {
            "value_names": [
                {
                    "name": "22"
                },
                {
                    "name": "15"
                }
            ],
            "system_name": "testik5",
            "version": 3,
            "in_use_indicator": "active"
        }
    ]
}

```