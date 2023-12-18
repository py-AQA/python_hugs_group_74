## 1. /api/v1/Activities GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:37 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 1,
    "title": "Activity 1",
    "dueDate": "2023-12-18T21:13:38.1580493+00:00",
    "completed": false
  },
  {
    "id": 2,
    "title": "Activity 2",
    "dueDate": "2023-12-18T22:13:38.1580517+00:00",
    "completed": true
  },
  {
    "id": 3,
    "title": "Activity 3",
    "dueDate": "2023-12-18T23:13:38.1580521+00:00",
    "completed": false
  }
]
```

## 2. /api/v1/Activities POST

* HTTP-метод: **POST**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 4,
  "title": "Activity 4",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": false
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:37 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Activity 4",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": false
}
```

## 3. /api/v1/Activities/3 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/3
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:38 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 3,
  "title": "Activity 3",
  "dueDate": "2023-12-18T23:13:38.673511+00:00",
  "completed": false
}
```

## 4. /api/v1/Activities/2457660577 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/2457660577
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:38 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-c361f64a5692fe408b2cf5cb5ac944cf-4d65407656e97c40-00",
  "errors": {
    "id": [
      "The value '2457660577' is not valid."
    ]
  }
}
```

## 5. /api/v1/Activities/8 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/8
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 8,
  "title": "Activity 8",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": true
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:38 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 8,
  "title": "Activity 8",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": true
}
```

## 6. /api/v1/Activities/8181935979 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/8181935979
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 8181935979,
  "title": "Activity 8181935979",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": true
}
```
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:39 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-bb0dfb906d7962459ed6df8418e4c8ff-0e3a6d82b6d89a4d-00",
  "errors": {
    "id": [
      "The value '8181935979' is not valid."
    ],
    "$.id": [
      "The JSON value could not be converted to System.Int32. Path: $.id | LineNumber: 0 | BytePositionInLine: 17."
    ]
  }
}
```

## 7. /api/v1/Activities/7 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/7
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Mon, 18 Dec 2023 20:13:39 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 8. /api/v1/Activities/9535816741 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/9535816741
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:39 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-641bf25be1f7f648a9ccd634c928d5b5-21869ddf994c4140-00",
  "errors": {
    "id": [
      "The value '9535816741' is not valid."
    ]
  }
}
```

## 9. /api/v1/Authors GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:39 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 1,
    "idBook": 1,
    "firstName": "First Name 1",
    "lastName": "Last Name 1"
  },
  {
    "id": 2,
    "idBook": 1,
    "firstName": "First Name 2",
    "lastName": "Last Name 2"
  },
  {
    "id": 3,
    "idBook": 2,
    "firstName": "First Name 3",
    "lastName": "Last Name 3"
  }
]
```

## 10. /api/v1/Authors POST

* HTTP-метод: **POST**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 2,
  "idBook": 1,
  "firstName": "First Name 2",
  "lastName": "Last Name 2"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:40 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 2,
  "idBook": 1,
  "firstName": "First Name 2",
  "lastName": "Last Name 2"
}
```

## 11. /api/v1/Authors/authors/books/3 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/authors/books/3
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:40 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 8,
    "idBook": 3,
    "firstName": "First Name 8",
    "lastName": "Last Name 8"
  },
  {
    "id": 9,
    "idBook": 3,
    "firstName": "First Name 9",
    "lastName": "Last Name 9"
  },
  {
    "id": 10,
    "idBook": 3,
    "firstName": "First Name 10",
    "lastName": "Last Name 10"
  }
]
```

## 12. /api/v1/Authors/authors/books/8994038381 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/authors/books/8994038381
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:40 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-a2a1965987c0fb4f9c0ffbd54dbd4865-6b1a72522916ec44-00",
  "errors": {
    "idBook": [
      "The value '8994038381' is not valid."
    ]
  }
}
```

## 13. /api/v1/Authors/5 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/5
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:41 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 5,
  "idBook": 2,
  "firstName": "First Name 5",
  "lastName": "Last Name 5"
}
```

## 14. /api/v1/Authors/5561763733 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/5561763733
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:41 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-ec50866da4f65f4f83055634eb193f74-b9f93f78d2da0b41-00",
  "errors": {
    "id": [
      "The value '5561763733' is not valid."
    ]
  }
}
```

## 15. /api/v1/Authors/1 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/1
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 1,
  "idBook": 1,
  "firstName": "First Name 1",
  "lastName": "Last Name 1"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:41 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 1,
  "idBook": 1,
  "firstName": "First Name 1",
  "lastName": "Last Name 1"
}
```

## 16. /api/v1/Authors/7399145279 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/7399145279
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 7399145279,
  "idBook": 1,
  "firstName": "First Name 7399145279",
  "lastName": "Last Name 7399145279"
}
```
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:41 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-184aecb590b12d4a8f9dc3fbee2d60e1-425da4ce68820e4d-00",
  "errors": {
    "id": [
      "The value '7399145279' is not valid."
    ],
    "$.id": [
      "The JSON value could not be converted to System.Int32. Path: $.id | LineNumber: 0 | BytePositionInLine: 17."
    ]
  }
}
```

## 17. /api/v1/Authors/9 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/9
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Mon, 18 Dec 2023 20:13:42 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 18. /api/v1/Authors/9319700929 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/9319700929
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:42 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-c0e01dd0cbbf1b4ca2df1e509532dec0-65fb8f3305066248-00",
  "errors": {
    "id": [
      "The value '9319700929' is not valid."
    ]
  }
}
```

## 19. /api/v1/Books GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:42 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 1,
    "title": "Book 1",
    "description": "Et minim possim amet doming amet amet amet dolore ea qui ipsum duis et et dolor. Sed duo magna assum. Et est vulputate labore consequat dolor commodo sed aliquyam eos nostrud vero et. Nostrud amet diam dolore nibh tempor est duo aliquyam no amet lorem sed. Rebum esse in vero.\n",
    "pageCount": 100,
    "excerpt": "Duis dolor nulla veniam minim consetetur ea vel ut duis lorem eros diam invidunt dolor amet. Dolor lorem praesent. Ipsum vero feugiat et lorem diam soluta stet nostrud et eirmod sed magna sit. Lorem labore ut gubergren diam facilisis et dolor aliquam no accusam clita minim justo laoreet in qui. Amet congue minim. Consetetur amet sanctus stet nulla consetetur delenit et dolore aliquyam nonumy et sed nihil kasd nam amet. Luptatum est est voluptua sed euismod diam amet. Eos molestie et dolore dolores dolore.\nAliquyam gubergren nonummy lorem et aliquam facer gubergren sed et eirmod sed sed sit rebum vel tempor. Iusto magna duo et lorem. Amet feugait sed ad ea duo. Ut nonumy sed et aliquyam duo diam sadipscing duo. Ea tempor qui dolor dolores lorem et accumsan aliquyam consetetur aliquam diam esse diam dolores kasd. Labore magna illum diam sit sanctus ea. Eirmod odio erat dolores et facer lorem velit dolor dolor. Nibh accusam dolore duo dolor nonumy labore. Eos rebum justo dolor magna ea amet vel nonummy aliquip vero et dolore possim at nulla ut. Et dolor erat zzril vero iriure tempor vel amet vel. Clita erat tempor kasd consequat sadipscing feugiat amet eirmod lorem volutpat dolore sea elitr labore. Et ut sed. Tempor et dolore duo invidunt vulputate nibh nibh diam. Voluptua justo dolore magna ipsum at tempor no aliquyam duis te sed luptatum accusam justo lorem. Takimata labore erat eirmod vero at et ea eu laoreet. Vero stet dolor nonumy at eos veniam ea ea voluptua nonumy nonummy tempor vero nulla nostrud nonumy voluptua dolores. Sed iusto eos justo nonumy sed. Volutpat sadipscing et. Eos dolor dolores ut ea kasd accusam tempor consetetur elitr vero et sit duo dolor feugiat.\nIllum consetetur eirmod amet. Elitr esse justo et labore ea erat. Liber sit te. Accumsan et et vero praesent consectetuer eos sed dolore lorem eirmod accusam illum vel vel autem velit illum voluptua. Facilisis et at ut stet augue tempor accusam ea dolore eirmod nam elitr dolor. Eros sed eos facilisis voluptua ea tempor sadipscing nonumy nihil duo eu nostrud wisi illum nonumy at. Et stet sed sit lorem eu eirmod eirmod ipsum eros rebum amet sit sed amet accusam accusam. Commodo praesent dolore consequat. Sed odio nisl sit magna sed tempor praesent elitr aliquyam accusam. Dolore vel veniam erat exerci eros consetetur augue quis. Et aliquyam nonumy kasd justo vel. Iusto sed invidunt duo kasd sit eum ut labore sanctus est. Gubergren accusam aliquip erat nobis ut quod at ipsum diam at dolore duis lorem sanctus lorem gubergren sanctus elit. Tation diam nonumy iusto ut in lorem. Et sanctus nulla et lobortis diam aliquip gubergren dolores amet takimata ipsum. Vero voluptua feugiat kasd duis justo kasd diam consetetur.\nDolor dolore nonummy dolore magna. Amet eos rebum erat. Rebum consectetuer aliquam dolores ipsum ut sit ea gubergren ipsum consequat amet labore lorem takimata vero. Suscipit mazim at kasd lorem delenit erat kasd est ut feugiat justo suscipit sit. Wisi est no amet at nibh dolores rebum eirmod erat dolor rebum lorem eum tempor diam. Iriure exerci amet accusam esse at ea dolores nulla sanctus dolor dolor sed duis iusto consequat. Soluta sit eum nulla sit tation in no ipsum dolore sit luptatum. Duo clita takimata lorem amet dolor labore voluptua hendrerit vel consetetur et ut accumsan justo et magna ut. Amet justo consetetur dolor magna ex eum dolor nibh diam dignissim sea stet. Praesent est invidunt sed tempor sit et lorem nonummy at et molestie te kasd tempor laoreet. Sanctus lorem ut dolores dolore. Zzril tation lorem duis sit takimata lorem takimata takimata aliquyam magna dolore ut labore voluptua. Dolor dolores sit sed dolor autem minim diam. Kasd est aliquyam ipsum gubergren voluptua amet elitr. Lorem ipsum dolores dolores at elitr euismod ex voluptua sea. In invidunt hendrerit in nostrud dolor vero labore. Tempor et lorem stet lorem eos. Aliquip elitr dolor takimata aliquyam.\nAugue diam amet dolores kasd at dolore dolore et est aliquyam sed id amet et. Stet magna et consetetur imperdiet tempor lorem nisl invidunt. Eos vero eros duis ex delenit labore ea hendrerit minim sit aliquyam consectetuer no dolor eos consetetur amet. No erat diam dolor at dolores id ea amet. Consetetur augue sed rebum takimata consequat vero. Kasd iusto wisi diam at. Erat ipsum dolore lorem takimata eros. Gubergren accusam amet consetetur vero ut diam lorem amet est elit labore elitr et ea quis. Ut vero kasd ex et in tempor duo invidunt adipiscing amet eirmod justo dolore sea lobortis dolor sit nibh. Ut ipsum consectetuer. Vulputate illum ad dolore sanctus invidunt no stet in et feugait et lorem facilisi voluptua delenit delenit diam. Laoreet sea et sadipscing consetetur in amet laoreet kasd ut aliquam erat voluptua sanctus no stet praesent eos aliquyam. Labore et vero nonumy lorem invidunt at sadipscing consetetur vero sed sea facilisis ea.\n",
    "publishDate": "2023-12-17T20:13:42.956472+00:00"
  },
  {
    "id": 2,
    "title": "Book 2",
    "description": "Et sed eos sed elit te sadipscing sanctus. Dignissim diam doming ut euismod diam diam sadipscing zzril tempor amet dolor eirmod nonumy no. Dolor dolor no eu elitr amet. Sadipscing vulputate sed voluptua justo ipsum ea vero aliquyam dolores tempor dolores dolore ipsum. Amet aliquyam tempor duo aliquyam duis dolor ullamcorper ut ipsum rebum takimata. Stet labore dolore sit justo dolor diam stet ipsum. Possim sit lorem erat tempor ut sit sanctus sea invidunt ad diam sanctus placerat vero et. Amet ut takimata takimata sanctus eirmod et amet sit. Invidunt dolor labore clita amet magna vel dolores iusto aliquyam praesent iriure accusam. Duis lorem et ea dolores lorem lorem dolor amet eirmod sed consetetur sit consetetur sit takimata vero duo elitr. Ea diam facilisis et duo duo duis at. Nonumy kasd duis sed eos eu sit dolores sea. Eos tempor no ipsum ea et sit esse tempor et eleifend eirmod zzril tempor sea duo et eum. Minim et elitr sed sadipscing gubergren diam sadipscing sed eos. Eu sed aliquip vero consequat kasd. Erat clita accusam praesent ipsum sit voluptua dolor volutpat et erat. Ipsum gubergren invidunt erat.\n",
    "pageCount": 200,
    "excerpt": "Dolore ut et est eirmod sed accusam stet et ut nostrud blandit diam duo ea duis. Illum duis lorem duo erat odio sed tation ipsum stet velit sit eos sadipscing placerat consetetur nulla nonumy. Sea eos vero sadipscing sea lobortis lobortis sea te ipsum nonumy amet quod sed et magna eos. Gubergren soluta erat euismod minim nonumy ea adipiscing kasd amet voluptua duo vero sed. Erat lobortis duo tation ipsum accusam consectetuer. Stet amet est tincidunt sit sit invidunt est ex erat et et volutpat ea nobis sadipscing labore. Te quod tation. In duis kasd elit ea in dolores rebum molestie facer eum amet elitr voluptua consetetur. Amet esse nisl consetetur sed justo tation sea sed augue dolor at ut vero. Eirmod enim ipsum nulla nulla praesent takimata zzril ad nonumy velit aliquyam consetetur vero takimata elitr. Dolore aliquam soluta et invidunt ad at eos diam tempor ut commodo dolor. Sanctus rebum sit lobortis at gubergren aliquip dolor augue nonumy nonumy nonumy est vel assum rebum labore.\nDoming elitr lorem et vero dolor est vero aliquam nisl rebum aliquam. Diam dolor et praesent ipsum sit adipiscing ipsum vero ea vero dolor et dolor facilisi takimata ex diam. Zzril clita consetetur amet dolor et nonumy liber facilisi invidunt magna dolore duo eleifend diam clita. Dolor tempor ea et diam elitr volutpat doming aliquyam quod diam est zzril consectetuer et nulla clita et invidunt. Autem et gubergren no augue eos. Elitr et et eum sadipscing ut congue est dolore kasd ea eum ipsum iriure iusto justo eu.\nSed ea et iusto et at lorem sed amet invidunt amet nonumy aliquyam. Dolor in clita et clita dolor ipsum dolores nulla ut luptatum voluptua commodo et gubergren. Exerci tincidunt kasd clita dolore voluptua diam gubergren ipsum ipsum labore nulla diam sit est vulputate aliquyam. Facilisi zzril kasd amet justo sit ipsum vero aliquam dolore takimata nonumy aliquyam accusam dolor sit. Blandit amet sadipscing dolores lorem ea ut.\nFeugait doming augue sadipscing autem at sit labore gubergren. Dolore diam et sadipscing ea sea nonumy eum lorem. Eos sit est tempor erat amet duis tempor voluptua accusam duis voluptua magna consetetur sadipscing odio sit iriure. Magna dolore elitr elit elitr dolor sit consetetur invidunt erat tempor dolore et. Consetetur odio tempor ipsum vel stet kasd commodo no. Eirmod kasd nulla amet ipsum dolores kasd eum nulla stet et eros magna. Autem ut et nulla feugait. Praesent diam augue stet tempor iusto lorem. Sit dolore in nobis. Ea in rebum dolor sit zzril et consectetuer adipiscing iusto sed eos justo sed sanctus. Feugait aliquyam eirmod eirmod labore sed ut gubergren rebum no laoreet sit sed consetetur iriure et takimata accusam. Ipsum ea sed magna sed est. Invidunt dolores esse possim qui amet clita diam voluptua sit tempor nostrud nonumy consequat at ipsum ea sadipscing nonumy. Sanctus lorem diam duo praesent feugiat in sea sanctus duo. Diam labore voluptua in delenit diam. Eos gubergren eirmod ipsum duo te ex. Adipiscing dolor nonumy eirmod amet labore eirmod invidunt sit volutpat diam. Tempor tempor nulla lorem ut voluptua. Diam sed adipiscing no consetetur lorem in in nihil zzril esse illum sit duo diam ut autem.\nEirmod duis eirmod magna euismod amet vero accumsan invidunt invidunt. Soluta aliquip sed mazim nonummy dolore lorem labore facilisis. Justo et suscipit dolore ut autem facilisi lobortis. Dolor dolore ut ex ullamcorper magna nonumy autem takimata. Magna sed dignissim dolor sit dolor aliquyam elitr nulla. Sed ut vero invidunt et et. Ipsum erat diam duis dolores eirmod labore illum. Sit est lorem justo diam ipsum sadipscing aliquam sadipscing sanctus soluta eu. Vero tempor sanctus rebum augue at soluta. Kasd luptatum sed clita vero ipsum et tempor ut nulla et velit quis erat tation takimata nonumy vulputate eirmod. Aliquam dolor sed consectetuer sit aliquam est tempor facer et euismod dolor et magna diam nam. Sea rebum amet diam ipsum sea kasd invidunt no tempor doming consetetur volutpat at amet vulputate gubergren ut rebum. Sea ea vero lorem erat delenit duis labore aliquam lorem. Takimata lorem consetetur magna eos eirmod et dolore diam eum sit consequat gubergren feugiat ullamcorper eos amet. Feugiat lorem takimata nibh duo est in diam ut erat et sadipscing dolore vel gubergren. Eirmod diam vero consetetur nonumy autem amet facer at no illum consequat sea accusam nisl placerat et lorem. Delenit voluptua magna tempor diam nonumy et lorem stet kasd aliquyam consectetuer kasd sanctus no accusam labore lorem. Elitr aliquyam dolore dolore praesent elitr facilisi sed dolore ea takimata lorem accusam feugiat. Dolor sit diam ipsum dolores lorem est iriure vero elit.\n",
    "publishDate": "2023-12-16T20:13:42.9565911+00:00"
  },
  {
    "id": 3,
    "title": "Book 3",
    "description": "Ut tincidunt ipsum ea tempor hendrerit et eum amet ipsum et ea sed consectetuer consetetur. Nonumy aliquyam nulla no lorem ut in at amet magna dolore consequat. Et suscipit est iusto dolor eos vel illum sit lorem takimata sit dolore duo sed magna.\n",
    "pageCount": 300,
    "excerpt": "Lorem gubergren in. Consetetur amet invidunt takimata duo labore laoreet lorem. Te placerat gubergren sed vel ea. Magna quis tempor zzril vero gubergren eirmod sea voluptua sit feugiat gubergren. Sanctus duis lorem nulla consectetuer exerci est volutpat diam iusto soluta consetetur ut nihil magna nonumy diam sadipscing magna. Dolore consetetur sadipscing commodo vulputate dolore ut. Sed ut volutpat dolore amet diam adipiscing stet lorem nonummy nonummy et sadipscing sanctus sed tempor et nisl. Magna hendrerit stet et ut illum feugait sadipscing kasd duo invidunt nonumy amet eros. Nulla lorem sanctus sit diam at clita. Et te luptatum kasd elitr sadipscing ipsum est sed justo diam eirmod vulputate ea. Diam consectetuer placerat sit velit amet duo lorem diam minim option ipsum tempor dolore eum consetetur te duo et. Sanctus voluptua et dolores eleifend sea clita consetetur accusam eos lorem. Nonummy ut lorem option est feugiat vero sanctus vero est tincidunt volutpat sadipscing eum dolores. Dolores ut dolores in stet tincidunt stet rebum clita diam ea aliquyam et vero ut molestie et ut. Sit soluta sadipscing nulla consetetur consetetur justo eirmod dolor et. Iriure et ut nonumy doming feugiat nonumy duo erat amet eos labore in ea dolores consetetur invidunt amet. Dolor no cum elitr et possim ut adipiscing dolor erat consetetur erat duis clita sanctus autem. Justo sadipscing nihil eirmod dolore sea sit dolor sed.\nId nonummy et quis et dolore enim erat nonumy duis et ea. Dolor minim sanctus ut hendrerit amet accusam vel sit dolore est dolor dolore magna lorem et sea laoreet eirmod. Amet diam stet erat congue dolor facilisis dolor nulla no et nihil sea. Et dolores dolor consetetur et dolores aliquyam sed sed ipsum amet. Duis dolor enim gubergren ea sed tempor dolor et. Blandit voluptua sanctus sadipscing zzril sed. Sed hendrerit tempor eirmod sit dolore invidunt. Rebum justo et elitr sea sit gubergren duo aliquyam duo at lorem autem sed sed tation clita soluta erat. At eirmod diam invidunt justo invidunt invidunt erat dolores eu zzril amet sed elitr dolores sit. Sanctus ea gubergren hendrerit no. Vero ipsum clita sed rebum consequat consequat diam clita takimata invidunt exerci sed. Ut eos est gubergren ea amet magna blandit dolor et sanctus sadipscing diam. Diam sit facilisi et gubergren adipiscing. Dolores sanctus amet et duis dolore dolor labore est elitr lorem voluptua tempor magna enim gubergren sit in sea. Sanctus justo elitr invidunt et. Sanctus accusam et praesent aliquyam erat facilisis dolores velit dolores facilisis eirmod.\nDuo ea dolor vel et duo tempor facilisis nam. Facilisi dolor at laoreet no dolor rebum at. Ipsum eu illum imperdiet. Kasd et et et augue commodo lorem clita dolor quod. Et eos stet sed dolor et diam eirmod. Gubergren consectetuer lorem eirmod tation assum dolor lobortis ut ut lorem dignissim justo laoreet consectetuer dignissim iusto dolores sit. Sanctus iriure at eleifend. Ut et illum delenit sit nihil dolor lorem enim imperdiet ipsum vel sadipscing elit voluptua delenit consetetur diam takimata. Dolores est wisi exerci vero magna accusam voluptua diam est et takimata dolor. Et sed justo diam ut liber invidunt nam eos aliquyam labore et consequat est voluptua sed dolores et justo. Tempor rebum erat takimata est et hendrerit voluptua est et stet sed sit at no magna elit. Tincidunt sit cum aliquyam aliquip ut vero ipsum praesent sit sit dolor sanctus eleifend nonumy nonummy dolor no blandit. Invidunt lorem sed feugiat et autem et dolore eos justo stet sed nibh stet diam sit eros laoreet. Sadipscing praesent sit ipsum elitr tincidunt. Diam feugiat duo eirmod sed amet vel justo duo.\nAt augue dolor. Elitr ut stet accusam et dolor sadipscing gubergren accusam amet accusam et. Sed invidunt sit dignissim lorem rebum sit. Rebum duo kasd rebum amet amet autem kasd sed ut stet gubergren sadipscing consetetur. Suscipit est nobis dolor amet et aliquyam in et ipsum. Sed et dolores accusam et. Tincidunt et sed delenit dolor sea facilisi aliquyam luptatum autem duis et consetetur. Ea labore aliquip odio magna accusam duo dolor ipsum blandit lorem nonumy consetetur. Et exerci euismod takimata eos diam est sed et lorem at ea gubergren. Nostrud placerat ea et. Dolor euismod takimata amet enim possim et dolore. Duo tation labore aliquyam rebum ipsum diam lorem justo aliquip ut elit. Eirmod duo vel. Molestie quis dolores takimata accumsan sit tempor id elitr dolor rebum sit ea tempor ea.\nNo vero in. Duo adipiscing vero et iusto dolor tempor et vulputate in eirmod amet labore est at magna. Clita te takimata tempor est duis clita vero lorem dolor aliquip magna et augue augue no lorem gubergren erat. Elit ipsum ipsum diam kasd vero et voluptua in ea eos sea justo ea sit rebum. In sit invidunt kasd magna et facilisis dolor ut nisl vulputate quod nonummy. Accusam clita eirmod amet gubergren tation consectetuer sadipscing magna stet invidunt et nonumy et duis erat justo. Rebum kasd dolore et consetetur kasd cum. Sea eirmod nibh et hendrerit dolor dolores justo quis aliquyam aliquyam dolore ut et diam ea. Et at dolor sadipscing no. Facilisi esse at dolor feugiat adipiscing. Duo sanctus vel takimata amet nihil vel clita hendrerit soluta dolores accusam feugiat. Et ipsum amet tation ea aliquyam liber accusam. Takimata voluptua congue et labore ipsum praesent suscipit justo justo sed magna vero dolor. Elitr labore rebum lorem aliquip sed no eos amet at eum.\n",
    "publishDate": "2023-12-15T20:13:42.9567049+00:00"
  }
]
```

## 20. /api/v1/Books POST

* HTTP-метод: **POST**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 3,
  "title": "Book 3",
  "description": "Description of book 3",
  "pageCount": 242,
  "excerpt": "Excerpt of book 3",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:43 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 3,
  "title": "Book 3",
  "description": "Description of book 3",
  "pageCount": 242,
  "excerpt": "Excerpt of book 3",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```

## 21. /api/v1/Books/3 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/3
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:43 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 3,
  "title": "Book 3",
  "description": "Eos dolor rebum at aliquip praesent takimata facilisis adipiscing. Gubergren eirmod no consequat aliquip dolor lorem consequat. Sadipscing sed erat nonumy at tempor et liber eos consetetur eirmod diam consequat sanctus elitr veniam amet. Amet id accusam quod takimata odio sit erat qui clita aliquam commodo. Lorem et et sanctus kasd ipsum dolor eirmod accusam sit sit labore. Nihil at autem dolore ipsum takimata duo gubergren lorem dolor consetetur. Amet voluptua labore et erat laoreet et eum. Et kasd stet lorem aliquyam sit magna. Vero gubergren tation quis ut at eos voluptua sanctus voluptua luptatum elit et amet rebum gubergren. Sea voluptua aliquyam et et stet dolor nulla velit rebum dolores et et ut dolor erat. Aliquyam elitr wisi sea clita dolor ea clita clita eum dolores stet accumsan gubergren dolor. Voluptua molestie justo duo aliquyam odio dolor dolor dolor magna. Diam sadipscing eos nonumy tempor sea et accusam. Voluptua ea lorem hendrerit ea dolor voluptua labore kasd dolor et ipsum justo nihil vero duo. Accusam amet facilisis consetetur est diam elit lobortis feugait justo diam sed commodo. Sea amet tation nulla kasd lorem eros justo illum sit feugiat esse et et eu accusam enim amet. Clita suscipit et stet sea lorem no diam ut takimata qui invidunt sadipscing vel facer takimata. Tempor et amet dolor enim dolor duo magna.\n",
  "pageCount": 300,
  "excerpt": "Stet veniam voluptua vero et diam. Tempor praesent elitr magna labore et dolor velit in sanctus ea sed esse lorem consequat no. Consetetur consetetur ut vero. Cum nobis et erat ut sit nisl. Labore sit sit eos. Et et dolor elitr wisi no kasd sed ullamcorper ea est tincidunt dolores. Et rebum erat aliquyam adipiscing aliquyam et ea nostrud praesent est assum accusam erat aliquyam diam. Stet magna eros rebum dolor sed ut sed ea rebum ipsum consetetur kasd vero stet dolor ex dolor sit. Et aliquyam dolore et takimata euismod. Ullamcorper diam ipsum magna kasd kasd amet gubergren kasd at dolor diam sanctus sed dolores lorem et et. Sadipscing diam ut stet volutpat sed labore odio tempor et eirmod ullamcorper sanctus eirmod invidunt facilisis sit veniam. Hendrerit eum dolores duo no sadipscing sed tation nonumy diam ea voluptua sed ad tempor eos. Et dolore duo ipsum diam euismod rebum tempor in amet facer et odio amet labore elitr amet. Iriure voluptua eos feugait consetetur stet ut consetetur.\nSed feugait diam et est est at. Consetetur sanctus duis dolores lorem vero duo vero adipiscing ipsum ipsum at et labore euismod. Stet et elitr. Illum esse ipsum et ut sed tempor dolor. Dolore dolores luptatum sea nonumy. Nam magna euismod eos ipsum sed ipsum at eu et aliquyam. Eos et lorem dolore et nonummy augue stet.\nVolutpat dolore vero eirmod et minim rebum. Lorem et voluptua sit et. Eirmod lorem consetetur molestie. Gubergren lorem sed est velit stet dolore sea sit. Et amet gubergren kasd sit adipiscing mazim dolore kasd et gubergren option clita eos gubergren nibh nisl. Lorem dolor labore stet. Accusam imperdiet accusam. Sed et vero tempor lobortis dolor adipiscing volutpat voluptua vel et sed elitr magna vulputate eirmod zzril. Feugiat elitr labore consetetur no sed nonumy no consetetur ut dolore justo est labore voluptua. Delenit sea tempor ut est dolore clita magna labore consetetur labore ea.\nEa tempor amet dolor duo quis sadipscing et stet illum. Sit sea molestie. Takimata dolore nonumy labore tempor consectetuer. Stet minim sit magna aliquyam diam gubergren ea takimata sanctus nobis sanctus et iriure sea tempor kasd. Minim nulla clita invidunt tempor feugiat vero eum nonumy kasd eu consetetur dolor. Accusam diam at augue tincidunt accusam illum et vero erat. Tation consetetur sit veniam sanctus ipsum consetetur takimata lorem vel. Dolores gubergren facilisis dolores takimata dolor velit volutpat dolor sit ipsum stet dolor ut et no duis amet. Erat ullamcorper ea at amet illum eos. Labore stet nonumy. Nihil amet et justo.\nFacilisi consectetuer dolore. Accumsan erat lorem iusto magna ut stet. Ex wisi elit no ea praesent dolor ut ut dolor labore justo dignissim est stet sea at duo illum. Est et diam clita congue justo dolore invidunt id magna duo facilisi et lorem no eos voluptua. Augue labore et aliquyam duis nonumy lorem vel vero aliquam et diam. Stet consequat magna aliquyam takimata voluptua enim sed sit adipiscing amet no elit. Diam duis et et nonumy et ut diam dolor lorem. Adipiscing labore delenit dolores. Dolore ut dignissim elitr lorem sanctus vulputate dignissim accusam ut nulla no luptatum erat. Esse eirmod ipsum sanctus dolore ipsum diam voluptua sea dolore hendrerit ea dolore tempor at dolor justo at volutpat. Facilisis ipsum eirmod facilisis et at sit sea iriure sea voluptua ut duo magna. Tempor aliquyam voluptua ut sea sea eu kasd clita erat elitr quod aliquip iriure voluptua. Dolore magna magna takimata lorem et gubergren. Diam ipsum ea blandit duo nisl justo ipsum labore magna ut sea. Sadipscing minim amet amet in gubergren eos erat sit enim. Et qui dolor iriure invidunt elitr takimata sanctus et diam stet est voluptua eros minim diam. Dolor no magna erat autem kasd nonumy ipsum tempor ut sanctus magna clita sea nonumy ipsum. Clita ipsum accumsan dolor amet elitr in nonumy takimata erat vel takimata dolor takimata amet et et. Sea ipsum duo enim no vulputate sanctus duis ut dolores iusto elitr aliquip tincidunt invidunt.\n",
  "publishDate": "2023-12-15T20:13:44.0278193+00:00"
}
```

## 22. /api/v1/Books/8763621171 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/8763621171
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:43 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-fa648258dbbe9d4088cb097715d4b039-10043cb811bd294a-00",
  "errors": {
    "id": [
      "The value '8763621171' is not valid."
    ]
  }
}
```

## 23. /api/v1/Books/4 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 4,
  "title": "Book 4",
  "description": "Description of book 4",
  "pageCount": 386,
  "excerpt": "Excerpt of book 4",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:44 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Book 4",
  "description": "Description of book 4",
  "pageCount": 386,
  "excerpt": "Excerpt of book 4",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```

## 24. /api/v1/Books/6452486518 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/6452486518
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 6452486518,
  "title": "Book 6452486518",
  "description": "Description of book 6452486518",
  "pageCount": 413,
  "excerpt": "Excerpt of book 6452486518",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:44 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-b9a4b5a95ce89c4db11f45a2d57abef8-bee48114c796eb43-00",
  "errors": {
    "id": [
      "The value '6452486518' is not valid."
    ],
    "$.id": [
      "The JSON value could not be converted to System.Int32. Path: $.id | LineNumber: 0 | BytePositionInLine: 17."
    ]
  }
}
```

## 25. /api/v1/Books/2 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/2
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Mon, 18 Dec 2023 20:13:44 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 26. /api/v1/Books/3854995420 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/3854995420
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:44 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-622d47bf749f674fad59e9d6f48deae8-8fbd416a192b4842-00",
  "errors": {
    "id": [
      "The value '3854995420' is not valid."
    ]
  }
}
```

## 27. /api/v1/CoverPhotos GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:44 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 1,
    "idBook": 1,
    "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
  },
  {
    "id": 2,
    "idBook": 2,
    "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 2&w=250&h=350"
  },
  {
    "id": 3,
    "idBook": 3,
    "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 3&w=250&h=350"
  }
]
```

## 28. /api/v1/CoverPhotos POST

* HTTP-метод: **POST**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 2,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:44 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 2,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```

## 29. /api/v1/CoverPhotos/books/covers/3 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/books/covers/3
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 3,
    "idBook": 3,
    "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 3&w=250&h=350"
  }
]
```

## 30. /api/v1/CoverPhotos/books/covers/5752757759 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/books/covers/5752757759
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-63b3e77360e98c41a27a35cdd0b0ac11-bcb3e3682ec2e84f-00",
  "errors": {
    "idBook": [
      "The value '5752757759' is not valid."
    ]
  }
}
```

## 31. /api/v1/CoverPhotos/4 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "idBook": 4,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 4&w=250&h=350"
}
```

## 32. /api/v1/CoverPhotos/9600461612 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/9600461612
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-266cb08342d8614fb1254090fcda5471-e805b28a291c5a47-00",
  "errors": {
    "id": [
      "The value '9600461612' is not valid."
    ]
  }
}
```

## 33. /api/v1/CoverPhotos/10 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/10
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 10,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 10,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```

## 34. /api/v1/CoverPhotos/8424184422 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/8424184422
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 8424184422,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:46 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-ca8916282ccb634fa6cbe8cb619a82c8-cca122d92f442c47-00",
  "errors": {
    "id": [
      "The value '8424184422' is not valid."
    ],
    "$.id": [
      "The JSON value could not be converted to System.Int32. Path: $.id | LineNumber: 0 | BytePositionInLine: 17."
    ]
  }
}
```

## 35. /api/v1/CoverPhotos/9 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/9
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Mon, 18 Dec 2023 20:13:46 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 36. /api/v1/CoverPhotos/6999964265 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/6999964265
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:46 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-55de316ca82a8a4ca81e73c6af676a24-bca2930bcdb53141-00",
  "errors": {
    "id": [
      "The value '6999964265' is not valid."
    ]
  }
}
```

## 37. /api/v1/Users GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:46 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 1,
    "userName": "User 1",
    "password": "Password1"
  },
  {
    "id": 2,
    "userName": "User 2",
    "password": "Password2"
  },
  {
    "id": 3,
    "userName": "User 3",
    "password": "Password3"
  }
]
```

## 38. /api/v1/Users POST

* HTTP-метод: **POST**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 9,
  "userName": "User 9",
  "password": "443154"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:46 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 9,
  "userName": "User 9",
  "password": "443154"
}
```

## 39. /api/v1/Users/6 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/6
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:46 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 6,
  "userName": "User 6",
  "password": "Password6"
}
```

## 40. /api/v1/Users/7861380529 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/7861380529
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:47 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-000d1844a3799841a4dabec98086ceb4-34dc70336cb72448-00",
  "errors": {
    "id": [
      "The value '7861380529' is not valid."
    ]
  }
}
```

## 41. /api/v1/Users/6 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/6
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 6,
  "userName": "User 6",
  "password": "945027"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Mon, 18 Dec 2023 20:13:47 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 6,
  "userName": "User 6",
  "password": "945027"
}
```

## 42. /api/v1/Users/5692104779 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/5692104779
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 5692104779,
  "userName": "User 5692104779",
  "password": "207371"
}
```
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:47 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-0c8cbee713c6454c88c0bb469569e062-c2d8e914a24e3149-00",
  "errors": {
    "id": [
      "The value '5692104779' is not valid."
    ],
    "$.id": [
      "The JSON value could not be converted to System.Int32. Path: $.id | LineNumber: 0 | BytePositionInLine: 17."
    ]
  }
}
```

## 43. /api/v1/Users/2 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/2
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Mon, 18 Dec 2023 20:13:47 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 44. /api/v1/Users/7438383291 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/7438383291
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **400 Bad Request**
* Заголовки ответа:
```
content-type: application/problem+json; charset=utf-8
date: Mon, 18 Dec 2023 20:13:47 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
  "title": "One or more validation errors occurred.",
  "status": 400,
  "traceId": "00-689ca01138a78747add753ea359a1a28-29c3ca5398cdca46-00",
  "errors": {
    "id": [
      "The value '7438383291' is not valid."
    ]
  }
}
```

