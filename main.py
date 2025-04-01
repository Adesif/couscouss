import requests
import time
import os
Localtime= time.localtime()

# https://discord.com/api/v9/channels/1198354384267002037/messages
content = input('content:\n')
with open("CouscousNumber", "r") as fichier:
    f= fichier.read()
    n=int(f) if f else 0
    print(n)
    

channelId = input('ChannelId\n')
token  = os.getenv("DISCORD_TOKEN")

julesChannelId = os.getenv('JULES_CHANNEL')

channelIdDict = {
    "jules": julesChannelId,
}
channelId = channelIdDict.get(channelId, None)
print(channelId)

payload = {
    'content': f"{content} n°{n}"

}

header = {
    'Authorization': token
}


while True :
    Localtime= time.localtime()
    if Localtime.tm_hour == Localtime.tm_min or (Localtime.tm_hour == 0 and Localtime.tm_min == 0):
        r = requests.post(f"https://discord.com/api/v9/channels/{channelId}/messages", data=payload, headers=header)
        r2 = requests.post(f"https://discord.com/api/v9/channels/1355228841630630160/messages", data=payload, headers=header)
        n+=1
        with open("CouscousNumber", "w") as fichier:
            f=str(n)
            fichier.write(f)
        
        payload['content'] = f"{content} n°{n}"

    
        print(r.status_code, Localtime.tm_hour, 'h ',Localtime.tm_min)
        time.sleep(3000)
    time.sleep(1)
