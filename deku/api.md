# /crawler/api/v1

## Domains

/domains [GET]
response:
```
{
  "data": [
      {
          "crawl_frequency_in_hours": 7,
          "name": "www.nedu.de",
          "last_crawled": null,
          "id": 5,
          "option_id": 1,
          "created_at": "2018-09-04T20:27:16.910805+00:00",
          "owner_id": null
      }
  ],
  "status": "success"
}
```

/domains [POST]
request:
```
{
	"name": "www.chefkoch.de",
	"option_id":1
}
```

response:
```
{
  "data": {
      "crawl_frequency_in_days": 7,
      "name": "www.chefkoch.de",
      "last_crawled": null,
      "id": 6,
      "option_id": 1,
      "created_at": "2018-09-05T07:46:24.176785+00:00",
      "owner_id": null
  },
  "status": "success"
}
```

/domains [PUT]
request:
```
{
	"name": "www.neu.de",
	"id": 6,
	"option_id":1
}
```

response: No Content [204]

/domains [DELETE]
request:
```
{
	"name": "www.neu.de",
	"id": 6,
	"option_id":1
{
```
reponse: No Content [204]



## crawl_options

/crawl_options [GET]
response:
```
{
    "data": [
        {
            "description": "This is quite funny",
            "name": "DEFAULT",
            "id": 1
        }
    ],
    "status": "success"
}
```

/crawl_options [POST]
request:
```
{
	"name":"Super funny",
	"description": "This is quite funny"
}
```

response:
```
{
    "data": {
        "description": "This is quite funny",
        "name": "Super funny",
        "id": 2
    },
    "status": "success"
}
```

/crawl_options [PUT]
request:
```
{
	"id":1,
	"name": "DEFAULT",
	"description": "This is the new description"
}
```
response: No content [204]

/crawl_options [DELETE]
request:
```
{
	"id":2,
	"name": "DEFAULTs"
}
```
reponse: No Content [204]

