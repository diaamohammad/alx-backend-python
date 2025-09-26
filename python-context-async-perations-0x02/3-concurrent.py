import asyncio
import aiosqlite



async def async_fetch_users():

    async with aiosqlite.connect('db_users') as db:
        db.row_factory = aiosqlite.Row
        async with db.execute('SELECT * FROM users') as cursor:
            users = await  cursor.fetchall()
            return [dict(user) for user in users] 
        

async def async_fetch_older_users():

    async with aiosqlite.connect('db_users') as db:
        db.row_factory = aiosqlite.Row
        async with db.execute('SELECT * FROM users WHERE age > 40') as cursor:

           users = await cursor.fetchall()
           return [dict(user) for user in users ]


async def main():

   users,older_users = await asyncio.gather(
    async_fetch_users(),
        async_fetch_older_users(),
        return_Exception= True
    )
   print("all users",users)
   print("users that bigger than 40 ",older_users)

if __name__ == '__main__':   

    asyncio.run(main())


