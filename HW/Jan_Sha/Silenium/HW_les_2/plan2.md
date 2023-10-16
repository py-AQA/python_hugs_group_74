1. Refactoring existing test
2. Add the necessary items to plan if this need
3. Add next test from the plan which were not written 

`План что буду делать по "пощупать сайт" https://www.saucedemo.com

Accepted usernames are:
    standard_user
    locked_out_user
    problem_user
    performance_glitch_user

pass: secret_sauce
`
1.
1.1 Проверка на наличие полей на странице авторизации: 

####    test_availability.py

   + - user_name 
   + - (Do have placeholder?)
   + - password 
   + - (Do have placeholder?)
   + - button

1.2. login verification: 

####    test_auth_all.py 

   + - войти под разными юзерами с валидными паролями
   + - check click Burger Menu
   + - logout system
   + - войти под разными юзерами с НЕ валидными паролями

1.3. Checking contents:

#### test_cheking_standart_user.py

    - the existence of the number of blocks
    - the existence of the number of image 
    - the existence of the number of button
    - the existence of a short description of products 
    - the existence of a cost products

    + Number of blocks is equel number of image, number of button, a short description of products 
    and a cost products and NOT empty

1.4. Add anything products to recycled

#### test_check_recycler.py
    
    + - add all items to the recycled 
    + - check items index from symbol recycled
    + - check items in the recycled, there must be number adding items

1.5. Remove added product from recycled
1.6. Continue shopping
1.7. First name, Second name, Zip_Code (valid or no?)
1.8. Finish button

2. Add items from the plan
2.1 Check sorted
    - using sorted A-Z
    - using sorted Z-A




2.2 Add items to Recycled from card items
2.3 Remove some items from Recycled