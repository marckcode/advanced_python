from contextlib import asynccontextmanager
import asyncio
import logging

import aiosqlite

#@asynccontextmanager
#async def get_connection():
#    conn = await acquire_db_connection()
#    try:
#        yield conn
#    finally:
#        await release_db_connection(conn)
        

#async def get_all_users():
#    async with get_connection() as conn:
#        return conn.query("SELECT ...")

async def main():
    logging.basicConfig(level=logging.INFO)
    async with aiosqlite.connect("application.db") as db:
        async with db.execute("SELECT * FROM blogs") as cursor:
            logging.info(await cursor.fetchall())
            
            
if __name__ == "__main__":
    asyncio.run(main())