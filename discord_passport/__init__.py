"""
discord-passport is a simple way to make a simple OAuth2 with the discord-api created by : iExi#0416
"""
import requests
import json

class Oauth2:
    def __init__(self,token,client_secret,client_id,redirect_uri):
        self.token = token
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def OAuth2Code(self,code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        json_data = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
        return json_data.json()['access_token']


class User:
    def __init__(self,access_token):
        self.code = access_token

    @property
    def getUserAvatar(self):
        json_data = requests.get("https://discord.com/api/v9/users/@me",headers={"Authorization": f"Bearer {self.code}"}).text
        json_data = json.loads(json_data)
        return f'https://cdn.discordapp.com/avatars/{json_data["id"]}/{json_data["avatar"]}.png '
    @property
    def getUserName(self):
        json_data = requests.get("https://discord.com/api/v9/users/@me",headers={"Authorization": f"Bearer {self.code}"}).text
        return json.loads(json_data)["username"]
    @property
    def getUserDiscriminator(self):
        json_data = requests.get("https://discord.com/api/v9/users/@me",headers={"Authorization": f"Bearer {self.code}"}).text
        return json.loads(json_data)["Discriminator"]
    @property
    def getUserPremiumType(self):
        json_data = requests.get("https://discord.com/api/v9/users/@me",headers={"Authorization": f"Bearer {self.code}"}).text
        return json.loads(json_data)["PremiumType"]
    @property
    def getUserEmail(self):
        json_data = requests.get("https://discord.com/api/v9/users/@me",headers={"Authorization": f"Bearer {self.code}"}).text
        return json.loads(json_data)["email"]
    @property
    def getUserFlags(self):
        json_data = requests.get("https://discord.com/api/v9/users/@me",headers={"Authorization": f"Bearer {self.code}"}).text
        return json.loads(json_data)["flags"]
