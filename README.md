# Alif Test project
___________________


### admin.py
__Module for administrator__ <br>
Can create rooms, that could be reserved.<br>
If some room were reserved, e.g. till 11.03.2025 <br>
Every admin enter will check, is dattime.now() > reserve_till date <br>
If yes, its mean that this room will be unreserved and will be free <br>
until new reserve <br>

### user.py
__Module for users__ <br>
Can reserve some room. Check which room is reserved for now or not <br>
If reserved some room, and datetime.now() > reserve_till date <br>
it means that reserve finished, and we can make new reserve <br>