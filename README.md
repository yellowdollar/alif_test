# Alif Test project
___________________


### admin.py
*** x Module for administrator x ***
Can create rooms, that could be reserved.
If some room were reserved, e.g. till 11.03.2025
Every admin enter will check, is dattime.now() > reserve_till date
If yes, its mean that this room will be unreserved and will be free 
until new reserve

### user.py
*** x Module for users x ***
Can reserve some room. Check which room is reserved for now or not
If reserved some room, and datetime.now() > reserve_till date
it means that reserve finished, and we can make new reserve