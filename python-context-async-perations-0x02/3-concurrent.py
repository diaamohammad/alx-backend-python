#!/usr/bin/env python3
"""
Concurrent Asynchronous Database Queries using aiosqlite and asyncio.gather
"""

import asyncio
import aiosqlite


async def async_fetch_users(db_name="db.sqlite3"):
    """Fetch all users"""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users(db_name="db.sqlite3"):
    """Fetch users older than 40"""
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()


async def fetch_concurrently():
    """Run both queries concurrently"""
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("All users:")
    for row in users:
        print(row)

    print("\nUsers older than 40:")
    for row in older_users:
        print(row)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
