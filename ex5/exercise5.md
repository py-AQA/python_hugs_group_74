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
date: Tue, 12 Dec 2023 08:01:35 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 1,
    "title": "Activity 1",
    "dueDate": "2023-12-12T09:01:36.6110175+00:00",
    "completed": false
  },
  {
    "id": 2,
    "title": "Activity 2",
    "dueDate": "2023-12-12T10:01:36.6110201+00:00",
    "completed": true
  },
  {
    "id": 3,
    "title": "Activity 3",
    "dueDate": "2023-12-12T11:01:36.6110204+00:00",
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
  "title": "Activity 4 7004",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": false
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:35 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Activity 4 7004",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": false
}
```

## 3. /api/v1/Activities/4 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:36 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Activity 4",
  "dueDate": "2023-12-12T12:01:37.2379766+00:00",
  "completed": true
}
```

## 4. /api/v1/Activities/270219 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/270219
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **404 Not Found**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/problem+json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:36 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404,
  "traceId": "00-540f63de5d87a447a11c963be428ecf0-577913fa7357eb4f-00"
}
```

## 5. /api/v1/Activities/4 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 4,
  "title": "Activity 4 8292",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": true
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:36 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Activity 4 8292",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": true
}
```

## 6. /api/v1/Activities/979530 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/979530
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 979530,
  "title": "Activity 979530 1625",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": false
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:37 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 979530,
  "title": "Activity 979530 1625",
  "dueDate": "2023-12-11T22:08:18.7373723+00:00",
  "completed": false
}
```

## 7. /api/v1/Activities/4 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:37 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 8. /api/v1/Activities/747536 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Activities/747536
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:37 GMT
server: Kestrel
```
* Тело ответа: **нет**

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
date: Tue, 12 Dec 2023 08:01:38 GMT
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
  "id": 4,
  "idBook": 1,
  "firstName": "First 4 4891",
  "lastName": "Last Name 4"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:38 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "idBook": 1,
  "firstName": "First 4 4891",
  "lastName": "Last Name 4"
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
date: Tue, 12 Dec 2023 08:01:38 GMT
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
  }
]
```

## 12. /api/v1/Authors/authors/books/463092 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/authors/books/463092
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:39 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[]
```

## 13. /api/v1/Authors/4 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:39 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "idBook": 1,
  "firstName": "First Name 4",
  "lastName": "Last Name 4"
}
```

## 14. /api/v1/Authors/890471 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/890471
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **404 Not Found**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/problem+json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:39 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404,
  "traceId": "00-be9736330f37fa43bed6f7b8a90f057e-f4dc334345cf3940-00"
}
```

## 15. /api/v1/Authors/4 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 4,
  "idBook": 1,
  "firstName": "First 4 8202",
  "lastName": "Last Name 4"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:40 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "idBook": 1,
  "firstName": "First 4 8202",
  "lastName": "Last Name 4"
}
```

## 16. /api/v1/Authors/312629 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/312629
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 312629,
  "idBook": 1,
  "firstName": "First 312629 7021",
  "lastName": "Last Name 312629"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:40 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 312629,
  "idBook": 1,
  "firstName": "First 312629 7021",
  "lastName": "Last Name 312629"
}
```

## 17. /api/v1/Authors/4 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:40 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 18. /api/v1/Authors/643898 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Authors/643898
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:40 GMT
server: Kestrel
```
* Тело ответа: **нет**

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
date: Tue, 12 Dec 2023 08:01:41 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[
  {
    "id": 1,
    "title": "Book 1",
    "description": "Est rebum accusam at sadipscing consetetur magna labore eos. Ipsum eum diam aliquyam ad aliquyam feugait quis invidunt sed sed accumsan lorem sed. Commodo vulputate takimata consectetuer congue erat invidunt dolore aliquyam gubergren no sit est gubergren elitr amet tempor et duo. Nisl et facilisis lorem est ut velit. Delenit autem dolores sit. Commodo diam elit ut ut duo ut gubergren. Quis labore delenit ut dolor stet aliquyam clita euismod. Invidunt diam kasd ut magna et tempor. Et sanctus invidunt sit labore erat rebum.\n",
    "pageCount": 100,
    "excerpt": "Sea et eu aliquyam tempor et sed vel sed ea justo liber vero diam sanctus facilisis lorem amet. Ut elit diam sanctus accusam ipsum sit qui est ex nulla sed labore sit diam elit nonumy justo. Tempor accusam sadipscing no autem. Vero iriure at. Invidunt nihil zzril et diam sadipscing sanctus duis mazim consequat consequat at. Vulputate et amet. Eos eu eos accusam sanctus et blandit et sed consetetur sea et takimata. Consectetuer vulputate sanctus labore voluptua quod tation consequat feugait blandit iusto. Stet sed stet adipiscing et dolore et accusam dolores no et et amet sed molestie gubergren. Diam invidunt dolore eos et. Et at vero ut eos iriure accusam velit. Ut sit eu ipsum. Vel justo ut ipsum labore vero erat sit aliquip ipsum.\nVero et et ea lorem commodo erat commodo iriure elit diam adipiscing vero sanctus sadipscing invidunt sit ut. Eros nostrud no et tincidunt eu blandit option sadipscing sed erat sea tation ipsum et est clita. Amet lorem imperdiet erat feugait et enim dolor doming et magna dolor praesent vero diam. Wisi ut lorem consequat dignissim odio sed. Eos gubergren vulputate et ipsum dolor sed eirmod stet et et veniam. Et invidunt dolore et odio wisi dolore no ipsum sit eros no sadipscing clita est ut consequat. Tincidunt nisl facilisis possim lorem sit tempor dignissim. Accusam ut voluptua nonumy sit luptatum sed. Quis amet eirmod sed. Vero lorem lorem eirmod magna diam et veniam stet eum duo ut ut sed labore diam magna. Est consetetur diam aliquyam eirmod magna sed. Laoreet eos sanctus diam lorem sit duis nibh dolores no ut sanctus dolores. Amet est hendrerit mazim dolor vulputate aliquip et no ad. Esse et dolor diam dolor nisl magna tempor labore consetetur amet dolor takimata erat ipsum magna amet. Dolore nonumy labore sed et justo elitr invidunt magna amet aliquyam amet no elitr. Et et dolor facer consetetur at laoreet tempor sanctus tempor invidunt tempor stet sed ut vel.\nKasd et sed at. Et ea aliquip sea diam imperdiet. Sed vel amet erat ea sanctus consequat ipsum labore ut in sed ullamcorper duo magna invidunt nulla tempor. Duis ipsum duis vero at et iriure et vero et vero. Invidunt dignissim sanctus lobortis et facilisis et.\nAmet labore tempor laoreet. Sanctus nonumy lobortis id elitr at diam accusam ut vero diam sit clita dolores sea duo dolor. No dolor aliquyam takimata amet consetetur sed et ea et placerat autem duo vero et. Et tempor consectetuer dolore labore consectetuer dolores et.\nHendrerit sit sed no nisl ipsum. Vel diam nonumy sit in elitr amet est ut magna. Consectetuer cum tation eos. Et wisi duo diam. Labore ex ipsum clita sadipscing kasd suscipit velit et consetetur ut vero. Accumsan nonumy dolores kasd sanctus stet sit sed et eu sed te. Et feugiat id minim sadipscing et. Et exerci et elitr gubergren ea sit lorem. Dolore blandit illum feugiat consetetur nonumy ea nonumy stet liber ipsum no vero kasd. Nonummy tincidunt exerci accusam kasd odio vero nulla duo accusam tation illum erat. Dignissim stet sit. Amet consetetur est nonumy. Accusam lorem dolore ea doming placerat esse eos eirmod. Voluptua eirmod duis facer aliquyam autem elitr adipiscing. Diam sed et ut tempor stet id est illum sed vel ex enim ut ex sit lorem. Ut zzril invidunt stet nonumy diam sed vel et ipsum nonummy ut. Dolore feugiat justo sadipscing nulla adipiscing gubergren diam accusam sanctus.\n",
    "publishDate": "2023-12-11T08:01:42.2433792+00:00"
  },
  {
    "id": 2,
    "title": "Book 2",
    "description": "Nisl eirmod magna luptatum. Diam gubergren gubergren. Ut facilisis erat blandit et et sit est ea. Amet magna nonummy lorem dolor lorem in autem rebum. Molestie eu ea. Commodo tempor sit clita elitr stet eos dolor accusam dolore dolor ipsum. Justo dolore consetetur no ipsum erat ipsum accusam kasd sit nonumy dolores praesent no odio sed nonumy feugiat sed. Aliquyam diam gubergren eu takimata. Dolor volutpat kasd nulla mazim elitr et sanctus nostrud dolor. Dolor tincidunt accusam accusam lorem ipsum nibh nulla sed et ut gubergren amet consectetuer kasd nonumy. Soluta ea delenit consequat option nostrud te ullamcorper amet ea amet takimata sed in voluptua facilisi et.\n",
    "pageCount": 200,
    "excerpt": "Dolores nonumy accusam et amet consectetuer amet eu at sed eos vel duo diam sanctus et sanctus duis at. Sadipscing gubergren sit vel rebum ut. Amet ea elitr eos magna veniam duis sit adipiscing ullamcorper. Sit ipsum diam diam elit sit et labore facilisi dolore. Est justo justo magna gubergren sed diam. Nonumy autem kasd at eirmod facilisis dignissim sea lorem. Nulla invidunt ea sea dolores sit rebum consetetur. Diam vel invidunt sadipscing placerat dolore zzril labore et sanctus aliquyam dolor.\nLorem clita ut. Facilisi sea stet erat duo luptatum est consetetur sed in. Sea sit elitr blandit et diam. Velit ipsum diam zzril te invidunt et eleifend justo lorem accumsan ipsum tempor sed. Ipsum takimata erat stet dolore tation lobortis. Tempor elitr kasd sit est stet diam nonumy ut gubergren tempor et ipsum sit liber esse dolores ut clita. Nostrud lorem invidunt wisi eum tation ipsum nulla ipsum feugiat exerci amet sed. Duis gubergren stet dolore no consetetur dolor duis te et. Dolores amet nibh rebum ipsum dolore sadipscing dolore gubergren sanctus sea magna et sit.\nQui at est volutpat labore labore. Dolor dolor ex dolore labore justo mazim consetetur aliquyam justo. Feugait eos aliquyam stet sit clita ea sed eirmod ipsum erat magna dolor sit amet velit labore. Feugait gubergren erat dolore dolor ut. Eirmod consetetur elitr ipsum accusam. Ullamcorper diam ad facer consequat justo sit erat et vero exerci. Amet sed ullamcorper ipsum dolore dolore diam eos dolor vel ut. Ipsum sanctus aliquyam. Ad sed illum sit lorem vel magna rebum. Eos sit sed sea kasd dolor sit iriure sed imperdiet voluptua consetetur sea sed ut. Vero consetetur option gubergren duo amet sadipscing in. Justo takimata sit eros magna exerci ea sanctus eirmod rebum ad ut eu sed eu dolore. Accusam voluptua lorem et nam feugiat. Duo eleifend magna nulla diam tempor at elit facilisi. Labore exerci dolores sed vero amet amet consequat kasd dolor. Est dolor est sea volutpat sit lorem tempor. At sit ea aliquam ipsum exerci voluptua kasd veniam.\nAt dolore accusam. Ea adipiscing amet sed vel kasd clita elitr voluptua. Diam accusam gubergren lorem et vero magna nonumy. Erat quis zzril sed ea et at ut consectetuer sed duo illum et gubergren eros amet est gubergren. Ipsum consequat nonumy blandit clita nonumy velit eum adipiscing. Erat consequat lorem gubergren nibh justo duis eum amet diam est invidunt eros minim stet. Sit magna duis no eos et clita at labore justo invidunt ipsum cum. Duo dolor eos no gubergren facilisis ut sed. Tempor sea dolor magna et invidunt. Eos aliquyam in consetetur praesent.\nNihil gubergren diam diam takimata vero. Sit et eirmod sit at at sanctus rebum. Ut et stet takimata tempor ad lorem eos aliquyam lorem. Gubergren nonumy ea enim elitr est amet consetetur magna. Consetetur takimata sed sadipscing lorem invidunt sanctus ipsum diam magna sanctus erat lorem ipsum adipiscing elitr et odio. At est at labore tincidunt illum dolores magna. Luptatum ipsum sea ipsum hendrerit hendrerit magna sit aliquyam. Lorem eum aliquip duis quis dolor ea rebum dolore aliquam lorem. Sea et diam ea. Et nulla diam sed nonumy invidunt wisi dolores sadipscing. Nostrud eos magna kasd ipsum duis magna id qui takimata accusam vero. Est sadipscing consetetur diam. Vel clita sed sea consequat lorem gubergren laoreet. Sadipscing consetetur soluta amet eirmod magna zzril accusam sanctus dolor dolor nonummy diam accusam.\n",
    "publishDate": "2023-12-10T08:01:42.2435178+00:00"
  },
  {
    "id": 3,
    "title": "Book 3",
    "description": "Amet rebum sed lorem no sed labore nonumy amet takimata ea ut clita duis. Luptatum vero eos vulputate diam illum justo est dolores sea clita eos luptatum at sadipscing nulla. Esse possim dolor. Nonumy suscipit dolor takimata accusam invidunt invidunt amet in vero et molestie amet dolores. Et at kasd vero rebum consetetur dolore takimata diam vero erat sadipscing eirmod ut consetetur. Lorem eos dolores eos. Euismod sea aliquyam ut dolor in consectetuer rebum no et vel. Molestie ipsum illum aliquyam. Amet laoreet autem et consectetuer luptatum dolor veniam sanctus voluptua id no. Voluptua aliquyam gubergren tincidunt lorem veniam adipiscing eos odio ea takimata magna dolor et eum rebum. Diam amet duo. Dolore enim facilisi lobortis sed tincidunt gubergren hendrerit illum ut liber dignissim sed commodo. Clita magna duis lorem invidunt amet no. Sit invidunt diam dolore duo amet amet sit dolore voluptua clita no tempor magna ut consectetuer. Gubergren est invidunt et nibh lorem et no. Voluptua elitr dolor nulla illum sed facilisis tincidunt.\n",
    "pageCount": 300,
    "excerpt": "Erat dolore sit consetetur suscipit magna. Vero sea takimata sit illum. Ipsum voluptua sadipscing ea ea accumsan dolore aliquam sit volutpat clita. Et nonumy erat sit et euismod. Sed diam stet sit quis sadipscing et lorem est invidunt et eirmod est dolor et. Praesent esse dolores consequat iriure hendrerit justo elitr sanctus rebum nonumy et eirmod no tincidunt ipsum facer amet vero. Et et invidunt dolor voluptua. Sea ullamcorper stet ea. Nonummy elitr vero aliquyam dolores vel vero aliquyam molestie takimata et et. Laoreet tincidunt takimata magna dolore sea tempor sit sadipscing ut wisi aliquyam lorem.\nEt consectetuer eirmod dolore volutpat dolor tation iriure dolor voluptua nonumy commodo sit stet ipsum rebum. Magna consequat facilisis labore molestie sanctus molestie. Illum aliquyam wisi diam gubergren. Tempor et sit sit sit dolor tempor rebum clita. No et accusam sed accusam est amet rebum ut sit elitr diam vero ea stet illum. Amet dolor eos. Nonumy gubergren no invidunt exerci placerat dolor nonumy rebum erat tempor in ipsum. Sanctus eos laoreet dolore voluptua autem. Sit ea et aliquip tation lorem amet amet feugiat magna et. Et quis et vulputate est justo facilisis stet. Sed et clita takimata takimata. Odio duo diam nonumy sea dolor tempor facilisis elitr invidunt. Nobis illum dolor diam.\nDelenit aliquyam elitr zzril augue minim lorem sea quod. Et autem justo duo invidunt illum in facilisis dolore clita diam voluptua sed labore consetetur duo et. Et ipsum est vero no gubergren blandit dolore aliquyam et diam amet sed invidunt sed feugiat dolore ipsum. Exerci takimata wisi justo voluptua voluptua kasd aliquyam euismod invidunt dolore duis erat amet sed amet at. Nonumy nisl no accusam sadipscing id magna aliquyam molestie ipsum et at invidunt sea. Dolore kasd kasd vulputate odio at consetetur voluptua amet ipsum nulla duis. Est diam nonumy esse lorem gubergren at voluptua gubergren feugiat esse voluptua elitr. Est iriure dolor diam duo amet sadipscing. Aliquam dolore aliquyam ipsum tempor magna dolore dolor dignissim ipsum diam stet nisl nobis te qui. Diam et at.\nImperdiet iusto amet stet suscipit dolor lorem dolore facilisis takimata doming zzril gubergren. Elitr ea eu clita. Takimata sit accusam magna dolores dolore velit eos. Dolor ipsum lorem aliquyam ea ut ut no amet et ea imperdiet tempor lorem est sea. In dolor amet ut assum vel molestie gubergren luptatum sea no dolores consequat molestie nulla. Takimata ipsum voluptua lobortis sea est duis eros labore. Sit laoreet vero lorem eirmod suscipit et sed ut dolor dignissim. Rebum invidunt takimata nonumy euismod sed dolor amet minim at in consetetur. Clita diam et duo lorem doming dolores esse ipsum et at. Et ullamcorper dolor sadipscing nulla cum diam sadipscing sea sadipscing sanctus amet. Ipsum diam sit invidunt justo sit et vel autem erat amet dolore eros consetetur amet enim. Erat feugiat diam duo dolor aliquip dolores aliquam dolore et sed sed ipsum. Amet takimata clita justo et illum accusam. Nonumy eu odio vel lobortis diam dolore hendrerit elitr hendrerit sed mazim iusto lorem stet. Kasd nulla kasd sea dolor kasd erat. Invidunt est exerci eu sed elitr ut amet stet et diam erat nonumy velit kasd elit takimata dignissim hendrerit. Consetetur invidunt takimata tincidunt invidunt eirmod magna diam ipsum takimata amet diam nonumy.\nEst lorem et lorem elitr elit et diam ipsum. Autem eum sit ea takimata ut et. Invidunt eum invidunt dolore ipsum amet sit doming labore ut takimata et. Dignissim invidunt magna. Lorem diam labore eirmod erat dolore eleifend lorem no kasd duis amet iriure vero. Et dolor sit dolor. Lorem tempor et no. Dolor in dolores eirmod voluptua sadipscing consetetur labore gubergren dolor duo et et sanctus takimata volutpat. No at takimata consequat dolore nostrud est dolor elitr diam eu takimata clita duo blandit no stet stet diam. Amet iriure ipsum consetetur sit sanctus amet dolor gubergren consetetur eirmod et diam stet quis et diam et. Dolore est dolor at dolore sanctus clita et eos nulla nibh diam invidunt takimata esse gubergren et magna euismod. Iusto tempor sit et dolore no iriure. Sit diam dolor sed sanctus vulputate nonumy autem nostrud at accusam esse sadipscing.\n",
    "publishDate": "2023-12-09T08:01:42.2436865+00:00"
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
  "id": 4,
  "title": "Book 4 7043",
  "description": "Description of book 4",
  "pageCount": 312,
  "excerpt": "Excerpt of book 4",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:41 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Book 4 7043",
  "description": "Description of book 4",
  "pageCount": 312,
  "excerpt": "Excerpt of book 4",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```

## 21. /api/v1/Books/4 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:42 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Book 4",
  "description": "Justo rebum iusto elit blandit voluptua tempor quis ipsum ea ut dolor nulla justo. Consectetuer aliquyam amet aliquyam et. Amet labore esse nulla vero eos aliquyam elit veniam. Nostrud amet et et lorem feugiat lorem sanctus dolore consequat. Dolore vero consetetur doming et erat ipsum et justo feugait sit duo sed lobortis dolore eu. Sea te ut vero ipsum erat consetetur consequat ipsum illum et aliquip kasd mazim eos. Dolores accusam invidunt ut labore aliquip dolor. Erat takimata et et diam dolor ipsum vel elitr veniam nonumy dolore aliquyam. Amet sit dolores at labore. Lorem lorem diam lorem stet et nulla. Dolore et lorem praesent sanctus lorem. At dolor clita et lorem amet eos laoreet lorem nonumy aliquyam diam. Et facilisis justo et dolore dolor ut sea ipsum voluptua magna tation ipsum ut nonummy ea facilisi dolores elit. Ea elitr dolor feugait quod ea qui soluta sanctus clita at amet dolor. Stet diam duo dolor sea vulputate ipsum ipsum molestie diam accusam tincidunt ut eu kasd. Ex eu dolor diam euismod stet dolor sed labore eos dolore labore. Et voluptua accusam gubergren hendrerit. Blandit sit facilisis et sea clita dolore consetetur sed elit eos vero aliquyam sanctus vero.\n",
  "pageCount": 400,
  "excerpt": "Aliquyam odio elitr dolore amet diam amet invidunt dolores. Te ea elitr gubergren autem labore facer sed molestie gubergren labore clita wisi in dolore nonumy. Sed accumsan ipsum stet. Sit et tempor ipsum vero ut. Eos sed voluptua dolores rebum duo takimata kasd dolore tempor voluptua sanctus nulla voluptua eros et eirmod lorem. Ea takimata facilisis clita lorem diam labore labore justo lorem eos consetetur aliquyam ad clita magna commodo eirmod stet.\nEirmod amet facilisi amet ipsum dolor amet in tempor dolore ipsum dolor. Sit tincidunt eos dolor vero justo eum dolor rebum accumsan delenit eirmod. Et magna volutpat esse lorem aliquyam ut magna eu in accusam luptatum kasd ea consetetur lorem sanctus dolore ut. Amet dolore congue liber vero vulputate dolores te stet dolores amet clita et labore takimata. Amet ea feugait sadipscing amet takimata duo voluptua sed. Elitr invidunt sea duis qui consetetur accusam amet at et nulla sed ullamcorper. Accusam lorem takimata et nonumy iriure te et in feugiat takimata duis invidunt aliquam consetetur amet invidunt. Ad magna amet aliquam ut ea diam ad voluptua erat. Dolore dolor commodo et vero erat amet et. Lorem molestie duis aliquyam sit eum dolore nonumy. Amet sed sea consetetur ipsum eros voluptua cum elitr odio clita minim.\nEleifend duo dolore illum sed nonumy gubergren justo soluta sadipscing erat lorem dolor eum rebum sit. Duo amet accumsan et. Sanctus ipsum ut congue ut aliquyam et lorem et duis duis no eum justo accusam clita duo dolore. Ea eu no accumsan dolores rebum amet sanctus eos. Dolore congue sadipscing facilisis ut justo eos voluptua elitr at sed clita euismod diam erat. Lorem dolor erat dolore erat elitr no delenit est ipsum amet voluptua nonumy. Dolore sed tempor dolores sed exerci ipsum sit elitr accusam amet tempor rebum duis sea et. Elitr blandit no kasd et zzril dolor.\nClita ut invidunt ea accumsan magna tempor et. No dolore elitr et diam sit ullamcorper. Rebum at ipsum ipsum at lorem sit vulputate cum amet elitr sed consetetur duis. Gubergren consetetur ullamcorper diam dolor sit soluta gubergren clita tempor justo vel vero iusto duis tincidunt et gubergren vero. Ea kasd sit lorem ipsum et sed duo sit dolor. Et dolores diam placerat zzril clita dolor no diam. Facilisi magna dolor gubergren nobis iriure. Stet et est voluptua ut erat labore ipsum sit duis. Augue ut elitr dolor dolores magna no consequat vero tation. Sanctus lorem feugiat eu duo tempor. Nonumy dolores eirmod at sit erat in exerci. Consectetuer sanctus feugait lorem. Sed ut et ipsum.\nKasd facilisi et ea eirmod ea vel clita rebum elitr illum et sed ullamcorper ut sanctus. Augue consequat diam option aliquyam sit dolores stet takimata et eirmod diam consectetuer eum feugiat ipsum et dolore. Esse accusam stet sadipscing amet sit magna sadipscing diam voluptua est. Sit veniam praesent ipsum sed erat erat kasd facilisis diam voluptua stet kasd sed erat accusam mazim invidunt. Ipsum adipiscing vero nihil aliquyam tempor adipiscing amet dolores et aliquyam iriure exerci. Erat accumsan nisl eirmod eu consetetur sanctus amet lorem justo. Consequat justo sea ipsum eros eum sanctus at kasd lorem lorem dolore. Clita amet ipsum sit gubergren et aliquyam labore nisl wisi clita amet dolor erat. Ea volutpat dolor et accumsan eu eum dolor justo tempor dolor eirmod sit. Diam aliquyam labore ipsum sed nonumy ut kasd invidunt adipiscing dolor et est invidunt sed aliquyam lorem at. Adipiscing est est stet vel accumsan et. Amet augue possim et diam dolor duo. Tation adipiscing dolor elitr accumsan vulputate consequat et nibh et vel volutpat sit lorem nibh sit lorem. Consetetur hendrerit in sea. Accusam amet qui suscipit sea sed consetetur veniam. Kasd dolor justo. Consetetur clita ut aliquyam diam sed duo takimata stet eum facilisis consequat. Duo sed laoreet duis in esse sed magna sed et dolore diam labore vero. Lorem accusam sea sea duo congue accusam rebum facilisis rebum duis tation.\n",
  "publishDate": "2023-12-08T08:01:43.1384115+00:00"
}
```

## 22. /api/v1/Books/474022 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/474022
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **404 Not Found**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/problem+json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:42 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404,
  "traceId": "00-df342c5b948b714884f134e45befba04-1578c8d7447df04d-00"
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
  "title": "Book 4 4480",
  "description": "Description of book 4",
  "pageCount": 799,
  "excerpt": "Excerpt of book 4",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:42 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "title": "Book 4 4480",
  "description": "Description of book 4",
  "pageCount": 799,
  "excerpt": "Excerpt of book 4",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```

## 24. /api/v1/Books/722774 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/722774
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 722774,
  "title": "Book 722774 5910",
  "description": "Description of book 722774",
  "pageCount": 586,
  "excerpt": "Excerpt of book 722774",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:43 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 722774,
  "title": "Book 722774 5910",
  "description": "Description of book 722774",
  "pageCount": 586,
  "excerpt": "Excerpt of book 722774",
  "publishDate": "2023-12-10T22:15:35.6799574+00:00"
}
```

## 25. /api/v1/Books/4 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:43 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 26. /api/v1/Books/604091 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Books/604091
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:43 GMT
server: Kestrel
```
* Тело ответа: **нет**

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
date: Tue, 12 Dec 2023 08:01:44 GMT
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
  "id": 4,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:44 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
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
date: Tue, 12 Dec 2023 08:01:44 GMT
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

## 30. /api/v1/CoverPhotos/books/covers/109487 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/books/covers/109487
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
[]
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
date: Tue, 12 Dec 2023 08:01:45 GMT
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

## 32. /api/v1/CoverPhotos/733726 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/733726
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **404 Not Found**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/problem+json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404,
  "traceId": "00-47b901fcd7b45d41b2f9d24604f3cc83-656fbc8d9235e741-00"
}
```

## 33. /api/v1/CoverPhotos/4 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 4,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:45 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```

## 34. /api/v1/CoverPhotos/888969 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/888969
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 888969,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:46 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 888969,
  "idBook": 1,
  "url": "https://placeholdit.imgix.net/~text?txtsize=33&txt=Book 1&w=250&h=350"
}
```

## 35. /api/v1/CoverPhotos/4 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:46 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 36. /api/v1/CoverPhotos/894323 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/CoverPhotos/894323
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:46 GMT
server: Kestrel
```
* Тело ответа: **нет**

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
date: Tue, 12 Dec 2023 08:01:47 GMT
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
  "id": 4,
  "userName": "User 4 9756",
  "password": "985937"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:47 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "userName": "User 4 9756",
  "password": "985937"
}
```

## 39. /api/v1/Users/4 GET

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:47 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "userName": "User 4",
  "password": "Password4"
}
```

## 40. /api/v1/Users/461789 GET - несуществующий id

* HTTP-метод: **GET**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/461789
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **404 Not Found**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/problem+json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:48 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "type": "https://tools.ietf.org/html/rfc7231#section-6.5.4",
  "title": "Not Found",
  "status": 404,
  "traceId": "00-fdb365a79c6ab04e9d14bdab5a60226c-6aa487a4d36c924e-00"
}
```

## 41. /api/v1/Users/4 PUT

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 4,
  "userName": "User 4 2794",
  "password": "811315"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:48 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 4,
  "userName": "User 4 2794",
  "password": "811315"
}
```

## 42. /api/v1/Users/945906 PUT - несуществующий id

* HTTP-метод: **PUT**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/945906
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса:
```json
{
  "id": 945906,
  "userName": "User 945906 4776",
  "password": "945759"
}
```
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-type: application/json; charset=utf-8; v=1.0
date: Tue, 12 Dec 2023 08:01:48 GMT
server: Kestrel
transfer-encoding: chunked
```
* Тело ответа:
```json
{
  "id": 945906,
  "userName": "User 945906 4776",
  "password": "945759"
}
```

## 43. /api/v1/Users/4 DELETE

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/4
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:48 GMT
server: Kestrel
```
* Тело ответа: **нет**

## 44. /api/v1/Users/242503 DELETE - несуществующий id

* HTTP-метод: **DELETE**
* Полный URL запроса: https://fakerestapi.azurewebsites.net/api/v1/Users/242503
* Заголовки запроса: ```accept: text/json; v=1.0```
* Тело запроса: **нет**
* Статус-код ответа: **200 OK**
* Заголовки ответа:
```
api-supported-versions: 1.0
content-length: 0
date: Tue, 12 Dec 2023 08:01:50 GMT
server: Kestrel
```
* Тело ответа: **нет**

