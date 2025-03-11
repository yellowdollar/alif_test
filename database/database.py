import asyncpg
import asyncio
import json

from database.errors import DatabaseErrors

class DatabaseAdmin:

    def __init__(
        self, user: str, password: str, 
        database:str, host: str
    ):
        self.user = user
        self.password = password
        self.database = database
        self.host = host


    async def create_connection(self):
        try:
            dbcon = await asyncpg.connect(
                user = self.user,
                password = self.password,
                database = self.database,
                host = self.host
            )

            self.session = dbcon

            print("{\n'message': 'database connection created',\n'status_code':200\n}")
        except Exception as error:
            raise DatabaseErrors(
                message = f"Database Error: {str(error)}"
            )
        
    async def close_connection(self):
        if self.session is not None:
            await self.session.close()
            self.session = None

    async def create_room(self, room_name: str):
        try:
            await self.session.execute(
                '''
                    INSERT INTO tb_room(name)
                    VALUES($1)
                ''', room_name,
            )

            print('Room Created Successfuly')

        except Exception as error: 
            raise DatabaseErrors(
                message = f'Database Error: Create Room function: {str(error)}'
            )
        
    async def get_rooms(self, id: int = None):
        try:
            if not id:
                rooms = await self.session.fetch(
                    '''
                        SELECT * FROM tb_room
                    '''
                )
                rooms_list = []
                for room in rooms:
                    room_dict = {
                        'id': room[0],
                        'name': room[1],
                    }

                    rooms_list.append(room_dict)

                return rooms_list
            if id is not None:
                rooms = await self.session.fetch(
                    '''
                        SELECT * FROM tb_room
                        WHERE id = $1
                    ''', id,
                )
                
                if not rooms:
                    return 'No room with this id'

                room_dict = {}
                for room in rooms:
                    room_dict['id'] = room[0]
                    room_dict['name'] = room[1]

                return room_dict    
        except Exception as error:
            raise DatabaseErrors(
                message = f'Database Error: Get Rooms function: {str(error)}'
            )
        
class DatabaseUser:

    def __init__(
        self, user: str, password: str, 
        database: str, host: str
    ):
        self.user = user
        self.password = password
        self.database = database
        self.host = host

    async def create_connection(self):
        try:
            self.session = await asyncpg.connect(
                user = self.user,
                password = self.password,
                database = self.database,
                host = self.host
            )
        except Exception as error:
            raise DatabaseErrors(
                message = f'Database User: Connection side error: {str(error)}'
            )
        
    async def get_rooms(self):
        try:
            rooms = await self.session.fetch(
                '''
                    SELECT 
                        tb_room.id AS room_id, 
                        tb_room.name AS room_name, 
                        tb_reserve.reserve_from, 
                        tb_reserve.reserve_till
                    FROM tb_room
                    INNER JOIN tb_reserve ON tb_reserve.room_id != tb_room.id;

                '''
            )

            rooms_list = []

            for room in rooms:
                room_dict = {
                    'id': room[0],
                    'name': room[1]
                }

                rooms_list.append(room_dict)

            return rooms_list
        
        except Exception as error:
            raise DatabaseErrors(
                message = f'User Get Room error: {str(error)}'
            )
        
    async def get_reserved_rooms(self):
        try:
            rooms = await self.session.fetch(
                '''
                    SELECT 
                        tb_room.id AS room_id, 
                        tb_room.name AS room_name, 
                        tb_reserve.reserve_from, 
                        tb_reserve.reserve_till
                    FROM tb_room
                    INNER JOIN tb_reserve ON tb_reserve.room_id = tb_room.id;

                '''
            )

            rooms_list = []

            for room in rooms:
                room_dict = {
                    'id': room[0],
                    'name': room[1]
                }

                rooms_list.append(room_dict)

            return rooms_list
        
        except Exception as error:
            raise DatabaseErrors(
                message = f'User Get Room error: {str(error)}'
            )
  
    # async def reserve_room(self, data: dict):
    #     try:
    #         check_is_free_room = await self.session.fetch(
    #             '''
    #                 SELECT tb_room.id, tb_room.name, tb_reserve.reserve_from, tb_reserve.reserve_till
                    
    #             '''
    #         )
    #     except Exception as error:
    #         pass
    