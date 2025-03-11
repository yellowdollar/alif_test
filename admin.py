import asyncio

from database.database import DatabaseAdmin

database = DatabaseAdmin(
    user = 'postgres',
    password = '934007717',
    database = 'alif_test',
    host = 'localhost'
)

async def main():
    while True:
        print('1. Connect to database')
        print('2. Create Room')
        print('3. Get All Rooms')
        print('4. Get Room by id')
        print('q. Exit')

        action = input("Choose Action: ")

        if action == 'q':
            await database.close_connection()
            print('Closing Connection... Bye: ')
            break

        elif action == '1':
            await database.create_connection()
        elif action == '2':
            room_name = input('Input name for the room: ')
            await database.create_room(room_name = str(room_name))
        elif action == '3':
            rooms = await database.get_rooms(id = None)
            print(rooms)
        elif action == '4':
            id_input = int(input('Input ID of the room: '))
            rooms = await database.get_rooms(id = id_input)
            print(rooms)
        else: 
            print("Please, Choose Correct action: ") 

if __name__ == "__main__":
    asyncio.run(main())