from steam import SteamID, WebAPI
import requests
import ast

allUsersGames = {}
i = 0
successes = []
failures = []

api = WebAPI(key="XXX")

allUsersGamesInfo = api.IPlayerService.GetOwnedGames(include_appinfo=True, appids_filter=100, include_played_free_games=True, steamid="XXX")

def helperSingleAppId(appId):
    requestURL = "https://store.steampowered.com/api/appdetails?appids=" + appId
    gameInfo = requests.get(requestURL)
    print(gameInfo)
    print(str(gameInfo.status_code))
    print(gameInfo.json())
    print(type(gameInfo.json()))
    if gameInfo.json() is None:
        print("its none")
    if gameInfo.json()[str(appId)]['success'] is True:
        print("its not none")
    print(gameInfo.json()[str(appId)]['data']['genres'])

helperSingleAppId("XXX")


i=1
for game in allUsersGamesInfo['response']['games']:
   appId = game['appid']
   requestURL = "https://store.steampowered.com/api/appdetails?appids=" + str(appId)
   gameInfo = requests.get(requestURL)

   if gameInfo.json() is not None:
       if(gameInfo.json()[str(appId)]['success'] is True):
           print("its true!!!")
   else:
       print("its none")
   print(i)
   i = i + 1

for game in allUsersGamesInfo['response']['games']:
    gameGenre = []
    appId = game['appid']
    requestURL = "https://store.steampowered.com/api/appdetails?appids=" + str(appId)
    gameInfo = requests.get(requestURL)
    print(i)
    print(gameInfo)
    print("status is: " + str(gameInfo.status_code))
    if gameInfo.json() is not None:
        gameInfoAsJson = ast.literal_eval(str(gameInfo.json()))
        if gameInfoAsJson[str(appId)]['success'] is True:
            print(gameInfoAsJson[str(appId)]['success'])
            print("success turned out ot be true")
            for genre in gameInfoAsJson[str(appId)]['data']['genres']:
                gameGenre.append(genre['description'])
                allUsersGames[appId] = game['name'], round((game['playtime_forever']/60), 3), gameGenre
                successes.append(appId)
        else:
            print(gameInfoAsJson[str(appId)]['success'])
            print("success turned out to be false")
            failures.append(appId)

    else:
        print("gameInfo is null")
        failures.append(appId)
    i = i + 1
