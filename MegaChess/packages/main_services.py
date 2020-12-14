import json
import websockets
import random
from .classes.User import User


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    print(message)
    await websocket.send(message)
    print("Acción enviada")


async def start(auth_token):
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(auth_token)
    while True:
        print('connection to {}'.format(uri))
        async with websockets.connect(uri) as websocket:
            await play(websocket)


async def challenge(username):
    data = {
        "username": username,
        "message": "¿Pinta un challenge?"
    }
    await send(websocket, "challenge", data)

    print("Acción realizada: Enviar desafío\n")

"""
async def accept_challenge():
    await send(
        websocket,
        'accept_challenge',
        {
            'board_id': data['data']['board_id'],
        }
    )
    print("Acción realizada: Aceptar desafío.\n")

"""


async def play(websocket):
    send_challenge = True  # Set to false for tournaments, so I do not send challenges.

    response1 = await websocket.recv()
    print(f"< {response1}")
    data = json.loads(response1)

    users_list = data['data']['users_list']
    #  users_list.remove("guiojeda") # Uncaomment so I do not send challengs to myself, for sure.
    print(users_list)

    user_to = random.choice(users_list)  # Uncomment line to send challenge to random person
    #  user_to = "guiojeda"  # Uncomment this line to send challenge to myself.

    if send_challenge:
        await send(
            websocket,
            'challenge',
            {
                'username': user_to,
                'message': 'Pinta un challenge?'
            }

        )
        pass

    while True:
        try:
            response = await websocket.recv()
            print(f"< {response}")
            data = json.loads(response)

            if data['event'] == 'gameover':
                print(data['event'])
                pass
            if data['event'] == 'ask_challenge':
                # Currently: accepts challenges from anyone.
                await send(
                    websocket,
                    'accept_challenge',
                    {
                        'board_id': data['data']['board_id'],
                    },
                )
                print("Acción realizada: aceptar desafío")
            if data['event'] == 'your_turn':

                actual_turn = data['data']['actual_turn']
                user1 = User(actual_turn)

                coords = user1.decide_move(data)

                from_row = coords[0]
                from_col = coords[1]
                to_row = coords[2]
                to_col = coords[3]

                await send(
                    websocket,
                    'move',
                    {
                        'board_id': data['data']['board_id'],
                        'turn_token': data['data']['turn_token'],
                        'from_row': from_row,
                        'from_col': from_col,
                        'to_row': to_row,
                        'to_col': to_col,
                    },
                )

        except Exception as e:
            print('error {}'.format(str(e)))
            break
