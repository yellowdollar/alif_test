import asyncio
from datetime import datetime

from database.database import DatabaseUser


database = DatabaseUser(
    user = 'postgres',
    password = '934007717',
    database = 'alif_test',
    host = 'localhost'
)

async def main():
    await database.create_connection()
    while True:

        print('1. Get All Rooms')
        print('2. Reserve Room')
        print('3. Get Reserved rooms')
        print('q. Exit')

        action = input("Choose action: ")

        if action == "q":
            print('Close Connection... Bye')
            break
        
        if action == "1":
            rooms = await database.get_rooms()
            print('This rooms are free: ')
            print(rooms)
        elif action == "2":
            room_id = int(input("Input room id to reserve it: "))
            reserve_from = input("Input date reserve from: ")
            reserve_till = input("Input date reserve till: ")

            data = {
                'room_id': room_id,
                'reserve_from': datetime.strptime(reserve_from, '%d.%m.%Y'),
                'reserve_till': datetime.strptime(reserve_till, '%d.%m.%Y')
            }

            result = await database.reserve_room(data = data)
        elif action == "3":
            rooms = await database.get_reserved_rooms()
            print('This rooms are not free: ')
            print(rooms)


if __name__ == "__main__":
    asyncio.run(main())