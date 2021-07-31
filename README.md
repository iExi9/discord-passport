# Discord-Passport v0.3
## Way to make simple Discord OAuth2

### How it work?

`+pip install discord-passport`

# Make the Auth
```py
import discord_passport as dp

Oauth = dp.Oauth2(token="Bot Token",client_secret="Bot Client Secret ",client_id="Bot ID",redirect_uri="Oauth Redirect URL")




Oauth.OAuth2Code("Code from OAuth2Code")

print(Oauth.getUserAvatar) # Return AvatarLink 

print(Oauth.getUserName) # Return Name Like iExi

print(Oauth.getUserDiscriminator) # Return Discriminator Like #0416

print(Oauth.getUserPremiumType) # Return PremiumTypeLike 0 1 2

"""
0:None
1:Discord Nitro Classic
2:Discord Nitro Gaming 
"""

print(Oauth.getUserEmail) # Return Email like email@iexi.xyz

print(Oauth.getUserFlags) # https://discord.com/developers/docs/resources/user#user-object-user-flags
```

+ Any Error Contact me : iExi#0416
+ Or enter : [Developer Support](https://discord.gg/uvGN89fvFr)


