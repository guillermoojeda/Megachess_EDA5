import asyncio
from packages.main_services import start


if __name__ == '__main__':
    auth_token = "d281d156-e4a0-4e6f-aba7-9714c648cf96"
    challenges_issued = 0
    asyncio.get_event_loop().run_until_complete(start(auth_token))

# Alternatively, can use this:
"""
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        auth_token = sys.argv[1]
        asyncio.get_event_loop().run_until_complete(start(auth_token))
    else:
        print('please provide your auth_token')
"""
