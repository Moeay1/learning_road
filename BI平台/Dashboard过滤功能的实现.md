# Dashboard过滤功能实现

#### 1. 目前Dashboard配置

```json
{
  "user_name": "mafeifei",
  "dashboard_name": "007",
  "charts": [
        {
            "chart_name": "chart01",
            "w": 100,
            "h": 100,
            "GridX": 0,
            "GridY": 0
        },
        {
            "chart_name": "chart02",
            "w": 100,
            "h": 100,
            "GridX": 0,
            "GridY": 0
        }
    ],
  "created_time": 1545980328290,
  "updated_time": 1545980328290
}
```

#### 2. 改造方向

因为dashboard过滤属于面板全局过滤条件,所以需要将过滤相关的参数增加到面板配置中.

#### 3. 改造后传参数据格式

```json
{
    "user_name": "user_name",
    "dashboard_name": "dashboard_name",
    "charts": [
        {
            "chart_name": "chart01",
            "w": 100,
            "h": 100,
            "GridX": 0,
            "GridY": 0
        },
        {
            "chart_name": "chart02",
            "w": 100,
            "h": 100,
            "GridX": 0,
            "GridY": 0
        }
    ],
    "filter_type": "filter_type", # 过滤类型
    "filter_field": "filter_field", # 过滤字段
    "filter_value": "filter_value", # term过滤时,关键字value
    "gte": "gte", # range过滤时,时间范围左边界
    "lte": "lte" # range过滤时,时间范围右边界
}
```

#### 4. 面板所支持过滤类型

1. 关键词过滤(`term`)

   ```json
   {
       "term": {
           "field_name": "field_value"
       }
   }
   ```

2. 时间范围过滤(`range`)

   ```json
   {
       "range": {
           "field_name": {
               "gte": gte,
               "lte": lte,
               "format": "epoch_millis"
           }
       }
   }
   ```

