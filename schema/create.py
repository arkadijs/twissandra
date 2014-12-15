#from django.apps import AppConfig
from cass import session, keyspace

def create_table(table, ddl):
    rows = session.execute("select columnfamily_name from system.schema_columnfamilies where keyspace_name = '{}' and columnfamily_name = '{}'".format(keyspace, table))
    if not rows:
        session.execute(ddl)

def create_tables():
    if not session:
        return
    create_table('users', """
        CREATE TABLE IF NOT EXISTS users (
            username text PRIMARY KEY,
            password text
        )
        """)
    create_table('friends', """
        CREATE TABLE IF NOT EXISTS friends (
            username text,
            friend text,
            since timestamp,
            PRIMARY KEY (username, friend)
        )
        """)
    create_table('followers', """
        CREATE TABLE IF NOT EXISTS followers (
            username text,
            follower text,
            since timestamp,
            PRIMARY KEY (username, follower)
        )
        """)
    create_table('tweets', """
        CREATE TABLE IF NOT EXISTS tweets (
            tweet_id uuid PRIMARY KEY,
            username text,
            body text
        )
        """)
    create_table('userline', """
        CREATE TABLE IF NOT EXISTS userline (
            username text,
            time timeuuid,
            tweet_id uuid,
            PRIMARY KEY (username, time)
        ) WITH CLUSTERING ORDER BY (time DESC)
        """)
    create_table('timeline',"""
        CREATE TABLE IF NOT EXISTS timeline (
            username text,
            time timeuuid,
            tweet_id uuid,
            PRIMARY KEY (username, time)
        ) WITH CLUSTERING ORDER BY (time DESC)
        """)

# class Schema(AppConfig):
#     name = 'schema'
#     verbose_name = 'Create Cassandra schema'
#     def ready():
#         create_tables()
