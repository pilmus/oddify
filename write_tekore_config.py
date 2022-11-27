import tekore as tk


from dotenv import dotenv_values
config = dotenv_values(".env")

client_id = config.get('SPOTIPY_CLIENT_ID')
client_secret = config.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = config.get('SPOTIPY_REDIRECT_URI')

scope = input("Enter the scope for which you wish to request access:\n")


conf = (client_id, client_secret, redirect_uri)
file = f'tekore_{scope}.cfg'



token = tk.prompt_for_user_token(*conf, scope=getattr(tk.scope,scope))
tk.config_to_file(file, conf + (token.refresh_token,))