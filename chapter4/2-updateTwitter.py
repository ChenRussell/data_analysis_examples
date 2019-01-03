from twitter import *
import json

#Make sure to add the access tokens and consumer keys for your application
# t = Twitter(auth=OAuth("Access Token","Access Token Secret","Consumer Key","Consumer Secret"))
t = Twitter(auth=OAuth("838362266965692417-A0CAA5SGwHni5A6DsuEgJOdFhvVihgS","lazfefOHlRZgmqXBfp6IfMKrfrIHiAr4qkiZ33g6efR1q","eJDr2QY7oHP7wP1e0JOsA4IR1","rUAZQwjPumCuiXHZUXpYqkIIoPgqZhAhrtQNsJzMKv8IVRsUId"))
statusUpdate = t.statuses.update(status='this is a update twitter api test, and fuck u!')
print(json.dumps(statusUpdate,indent=1))