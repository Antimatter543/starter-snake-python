import os
import random
import json 
import cherrypy
from utils import * 




class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "antimatter543",  # TODO: Your Battlesnake Username
            "color": "#930318",  # TODO: Personalize
            "head": "sand-worm",  # TODO: Personalize
            "tail": "default",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json

        print("START")
        return "ok"


    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        data = cherrypy.request.json
        
        #### Snake Variables ####
        head =data['you']['head']
        neck = data['you']['body'][1]

		# foods = data['board']['food'] # [{x: ., y: .,}, ...]

        head_pos = (head['x'], head['y']) #(x,y)
        neck_pos = (neck['x'], neck['y'])
        print('head', head_pos)
        print('neck', neck_pos)

        #### Set up ####
        possible_moves = ["up", "down", "left", "right"]
        board = data['board']
        tick = data['turn']

        ### Debugging
        print("It's tick", tick)
        print("DATA", data)

        
        ## Logic ##
        
        # Stop from going off board by removing that move from the action space. Also stops snake from going into itself.
        for move in possible_moves: 
            potential_move = move_to_coord(move, head_pos) # (x,y)
            print("This is the move and potential move from the logic area", move, potential_move)
            if not (offBoard(board, potential_move) or equal_coords(potential_move, neck_pos)):
                print("We're moving here!", move)
                return {"move": move}

                print("I'm removing this move", move) # Removing this actually causes the list to shuffle back one, so it ends up skipping over a possible move. Which ends up making it kill itself.
                possible_moves.remove(move)
                
        # Choose a random direction to move in

        # print("TESTING", data['game']['id'])


        ## Decide move 
        move = random.choice(possible_moves)
        print("This is the final print statement before the next tick. I'll see you in the future, present me!")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)

