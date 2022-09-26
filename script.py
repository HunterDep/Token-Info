import requests, os, time, pyfiglet

def banner():
	print(pyfiglet.figlet_format("token info"))
	print("Github: https://github.com/HunterDep\nYouTube: https://youtube.com/channel/UCyo1KzxCt9iJybQPFXmMOPg\n")

def token_info(token):
	diruser = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token}).json()
	
	return diruser
	
banner()
token = input("[>] Coloque o Token: ")
print("Aguarde...")
time.sleep(1)
os.system("clear")
banner()

informações = token_info(token)

for informação in informações:
	texto = f"[{informação[0].upper() + informação[1:]}] {informações[informação]}"
	print(texto)
print(f"[Token] {token}")
