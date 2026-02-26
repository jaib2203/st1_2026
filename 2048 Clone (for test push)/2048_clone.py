# 2048_clone.py
# An attempt to re-create the game 2048 using pygame.

import pygame
import random

# pygame setup
pygame.init()

window_size = (600, 600)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
running = True
dt = 0 # Delta time - super important for frame-independent actions.


# Wrap the whole game code in a try/except block to see error outputs in the terminal.
try:

    # Game setup
    tile_size = (128, 128)
    tile_gap = 10
    window_offset = 30
    win_bool = False
    game_over_bool = False
    tile_moved = False
    button_cooldown = 0

    TILE_BG = pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\Tile Background.png").convert_alpha()
    tile_bg_scaled = pygame.transform.smoothscale(TILE_BG, tile_size)
    TILES = {
        2 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\2 Tile.png").convert_alpha(),
        4 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\4 Tile.png").convert_alpha(),
        8 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\8 Tile.png").convert_alpha(),
        16 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\16 Tile.png").convert_alpha(),
        32 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\32 Tile.png").convert_alpha(),
        64 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\64 Tile.png").convert_alpha(),
        128 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\128 Tile.png").convert_alpha(),
        256 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\256 Tile.png").convert_alpha(),
        512 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\512 Tile.png").convert_alpha(),
        1024 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\1024 Tile.png").convert_alpha(),
        2048 : pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\2048 Tile.png").convert_alpha(),
    }
    BACKGROUND = pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\Background.png").convert_alpha()
    bg_scaled = pygame.transform.smoothscale(BACKGROUND, (600, 600))
    TEXTBOX = pygame.image.load(r"C:\Users\Jai Butler\Documents\Python Programs\2048 Clone\assets\Bottom UI.png").convert_alpha()
    font = pygame.font.SysFont("Arial", 60, bold = True)
    win_text = font.render("YOU WIN!", True, (255, 255, 255))
    lose_text = font.render("GAME OVER...", True, (255, 255, 255))
    # This empty dict is generated when the game starts, with the positions of all 16 tiles. Eg:
    # {(1, 1): (30, 30), (1, 2): (168, 30), (1, 3): (306, 30), (1, 4): (444, 30)
    tile_positions = {}
    # An array containing data for every tile on the board. The arrays contain the following data:
    # [image filepath, grid coordinate (tuple), tile value, has_merged bool, pixel coordinate (list)] - could be improved by converting to a dict.
    active_tiles = []


    def render_background() -> None:
        # Fill the screen with an image to wipe away anything from last frame. 
        if game_over_bool:
            screen.fill("red")
        elif win_bool:
            screen.fill("green")
        else:
            screen.blit(bg_scaled, (0, 0))
        # Setting up the background tiles in a 4x4 grid.
        for row in range(4):
            for col in range(4):
                x = window_offset + col * (tile_size[0] + tile_gap)
                y = window_offset + row * (tile_size[1] + tile_gap)
                screen.blit(tile_bg_scaled, (x, y))
                tile_positions[(row + 1, col + 1)] = (x, y)


    # This runs constantly to render the active tiles every frame.
    def render_active_tiles() -> None:
        move_speed = 10.0

        for tile in active_tiles:
            # Get the current pixel position and the target position.
            current_pixel_pos = tile[4]
            target_pixel_pos = tile_positions.get(tile[1], (0, 0))

            # Calculate the difference for the x and y coordinates.
            diff_x = target_pixel_pos[0] - current_pixel_pos[0]
            diff_y = target_pixel_pos[1] - current_pixel_pos[1]

            # Animate the tile movement. 
            if abs(diff_x) > 0.1:        
                current_pixel_pos[0] += diff_x * move_speed * dt
            else:
                current_pixel_pos[0] = target_pixel_pos[0] # Snap to position.

            if abs(diff_y) > 0.1:
                current_pixel_pos[1] += diff_y * move_speed * dt
            else:
                current_pixel_pos[1] = target_pixel_pos[1]

            # Render the tile at the updated pixel position.
            screen.blit(tile[0], (current_pixel_pos[0], current_pixel_pos[1]))


    # A simple endgame textbox to show the player when they've won or lost.
    def render_endgame(type: str) -> None:
        # Render the textbox (box).
        box_pos = (10, 240)
        screen.blit(TEXTBOX, box_pos)
        
        # Get the rect of the textbox to use its center.
        box_rect = TEXTBOX.get_rect(topleft=box_pos)
        
        # Determine which text to use (loss or win).
        text = win_text
        if type == "loss":
            text = lose_text
        
        # Create a rect for the text and snap its center to the box's center.
        text_rect = text.get_rect(center = box_rect.center)
        screen.blit(text, text_rect)


    # When a new tile is spawned, this function determines whether it's a 2 or a 4 based on the weighted probabilities.
    def determine_spawn_type() -> list:
        rand = random.randint(1, 10)
        if rand > 9:
            return [TILES[4], 4]
        else: 
            return [TILES[2], 2]


    # Spawns two tiles when the game starts in random positions.
    def spawn_new_tile() -> None:
        # Create a list of legal positions using all tile_pos keys, but removing any that are in occupied positions.
        occupied_grid_positions = set()
        for tile in active_tiles:
            occupied_grid_positions.add(tile[1])
        legal_positions = [pos for pos in tile_positions.keys() if pos not in occupied_grid_positions]

        # Spawn 1 new tile.
        if legal_positions:
            pos = random.choice(legal_positions)
            legal_positions.remove(pos)
        else:
            return

        tile_type = determine_spawn_type()
        # [tile_type filepath string, position coord tuple, type_type int, has_merged bool]
        active_tiles.append([tile_type[0], pos, tile_type[1], False, list(tile_positions[pos])])

        #print(f"ACTIVE TILES: {active_tiles}")
        print(f"OCCUPIED POSITIONS: {occupied_grid_positions}")
    

    # Searches the active tiles array for a tile's value based on its coordinate.
    def get_tile(coord: tuple) -> list:
        for tile in active_tiles:
            if tile[1] == coord:
                return tile
        return []


    # Check whether two tiles can merge with each other.
    def check_merge(tile_1: int, tile_2: int) -> bool:
        #print(f"checking if {tile_1} and {tile_2} can merge.")
        if tile_1 == tile_2:
            print("merge permitted")
            return True
        return False


    # If two identical tiles "crash" into one another, merge them into the next number.
    # The merge will occur at the target tile's position.
    def merge_tiles(tile_1: list, target_tile: list) -> None:
        global tile_moved
        global win_bool

        # Ensure tiles don't merge twice in a turn.
        if tile_1[3] == True:
            return
        if target_tile[3] == True:
            return
        
        #print(f"MERGING: {tile_1} and {target_tile}")
        # The new value is just the current tiles' value multiplied by 2.
        new_tile_val = tile_1[2] * 2
        new_tile_pos = target_tile[1]
        new_tile_image = TILES[new_tile_val]
        new_tile_pixel_pos = tile_positions.get(new_tile_pos, (0, 0))

        # Remove existing tiles.
        active_tiles.remove(tile_1)
        active_tiles.remove(target_tile)

        # Spawn new tile.
        active_tiles.append([new_tile_image, new_tile_pos, new_tile_val, True, list(new_tile_pixel_pos)])
        tile_moved = True

        # Check for win state (2048 tile).
        if new_tile_val == 2048:
            print("YOU WIN!")
            win_bool = True
    

    # This checks if any merges are available before declaring game over.
    def check_game_over() -> None:
        global game_over_bool

        # Double check.
        if len(active_tiles) < 16:
            return
        
        # Create a quick lookup map so we don't have to loop over active_tiles repeatedly.
        tile_map = {tile[1]: tile[2] for tile in active_tiles}

        # Loop through active tiles and check each tiles' neighbours for merges. If one is allowed, return.
        for tile in active_tiles:
            x, y = tile[1]
            val = tile[2]
            
            # We only need to check right and down to cover all pairs without duplicates.
            for diff_x, diff_y in [(1, 0), (0, 1)]:
                neighbor_coord = (x + diff_x, y + diff_y)
                
                if neighbor_coord in tile_map:
                    if tile_map[neighbor_coord] == val:
                        # A merge is possible. Game not over.
                        return 

        # If we checked everything and found no permissable merges, then the game is over.
        print("GAME OVER!")
        game_over_bool = True


    # When input is provided (arrow keys), move all active tiles in that direction.
    def move_tiles(direction) -> None:
        global tile_moved
        # Checks if any tiles moved this press.
        tile_moved = False

        # Create a set of occupied grid positions so that tiles don't move into occupied spots.
        occupied_grid_positions = set()
        for tile in active_tiles:
            occupied_grid_positions.add(tile[1])

        #print(f"{direction} pressed")
    
        # Sort the active tiles array so that the tiles are moved in the right order.
        match direction:
            case "up":
                # In this lamba function [1] tells it to sort by the coord and the [0] tells it to sort by row.
                active_tiles.sort(key = lambda x: x[1][0]) 
            case "down":
                active_tiles.sort(key = lambda x: x[1][0], reverse = True)  # Reverse sorts from highest to lowest.
            case "left":
                active_tiles.sort(key = lambda x: x[1][1])
            case "right":
                active_tiles.sort(key = lambda x: x[1][1], reverse = True)
            case _:
                return

        active_tiles_copy = active_tiles.copy()

        for active_tile in active_tiles_copy:
            if active_tile not in active_tiles:
                continue
            
            # Convert the tuple into a list so it's mutable.
            coord_list = list(active_tile[1])

            # Create a copy of the current tiles coords so we can check the next step so tiles don't collide.
            next_step = coord_list.copy()

            # Tile has not merged this move.
            active_tile[3] = False

            # Move the tile in the direction specified by adjusting its grid position.
            match direction:
                case "up": 
                    while coord_list[0] > 1:
                        # First we check the next tile step to see if it's occupied.
                        next_step[0] -= 1
                        if tuple(next_step) in occupied_grid_positions:
                            #print("next step occupied. Checking for merge.")
                            # If it is occupied, see if a merge can occur.
                            target_tile = get_tile(tuple(next_step))
                            if target_tile:
                                if check_merge(active_tile[2], target_tile[2]):
                                    # If merge conditions are satisfied, merge the two tiles.
                                    merge_tiles(active_tile, target_tile)
                                # If no merge can occur, stop moving the tile.
                                #print("merge not permitted. Stopping tile.")
                                break
                        coord_list[0] -= 1 # Move towards row 1
                        # Checking mechanism to ensure index is never out of range.
                        if coord_list [0] < 1:
                            coord_list[0] = 1

                case "down": 
                    while coord_list[0] < 4:
                        next_step[0] += 1
                        if tuple(next_step) in occupied_grid_positions:
                            #print("next step occupied. Checking for merge.")
                            target_tile = get_tile(tuple(next_step))
                            if target_tile:
                                if check_merge(active_tile[2], target_tile[2]):
                                    merge_tiles(active_tile, target_tile)
                                #print("merge not permitted. Stopping tile.")
                                break
                        coord_list[0] += 1 # Move towards row 4.
                        if coord_list [0] > 4:
                            coord_list[0] = 4

                case "left": 
                    while coord_list[1] > 1:
                        next_step[1] -= 1
                        if tuple(next_step) in occupied_grid_positions:
                            #print("next step occupied. Checking for merge.")
                            target_tile = get_tile(tuple(next_step))
                            if target_tile:
                                if check_merge(active_tile[2], target_tile[2]):
                                    merge_tiles(active_tile, target_tile)
                                #print("merge not permitted. Stopping tile.")
                                break
                        coord_list[1] -= 1 # Move towards col 1.
                        if coord_list [1] < 1:
                            coord_list[1] = 1

                case "right": 
                    while coord_list[1] < 4:
                        next_step[1] += 1
                        if tuple(next_step) in occupied_grid_positions:
                            #print("next step occupied. Checking for merge.")
                            target_tile = get_tile(tuple(next_step))
                            if target_tile:
                                if check_merge(active_tile[2], target_tile[2]):
                                    merge_tiles(active_tile, target_tile)
                                #print("merge not permitted. Stopping tile.")
                                break
                        coord_list[1] += 1 # Move towards col 4.
                        if coord_list [1] > 4:
                            coord_list[1] = 4

                case _:
                    return
            
            # Assign the tile's new position in the active_tiles array and check if the tile moved.
            # This will auto move the tile as active_tiles are rendered every frame.
            new_coord = tuple(coord_list) # Convert back to tuple.

            if new_coord != active_tile[1]:
                tile_moved = True

            active_tile[1] = new_coord
            occupied_grid_positions.add(new_coord)

        # Spawn a new tile after every move
        if tile_moved:
            spawn_new_tile()
        
        # Check for game over state if there are 16 (or more, technically) occupied grid positions.
        if len(occupied_grid_positions) > 15:
            check_game_over()

    # Pre loop code (e.g. runs once at the start, instead of every frame).
    pygame.display.set_caption("2048 Clone")
    render_background() # Need to run this once at the start to get the tile positions array.
    spawn_new_tile()
    spawn_new_tile()
    

    while running:
        # Primary event code
        if button_cooldown > 0:
            button_cooldown -= dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and button_cooldown <= 0:
                if event.key == pygame.K_UP:
                    move_tiles("up")
                    button_cooldown = 0.1
                elif event.key == pygame.K_DOWN:
                    move_tiles("down")
                    button_cooldown = 0.1
                elif event.key == pygame.K_LEFT:
                    move_tiles("left")
                    button_cooldown = 0.1
                elif event.key == pygame.K_RIGHT:
                    move_tiles("right")
                    button_cooldown = 0.1
 

        # Game rendering.
        # Render background every frame.
        render_background()
        # Render all active tiles every frame.
        render_active_tiles()
        # Render the game over overlay when the game is over.
        if game_over_bool:
            render_endgame("loss")
        elif win_bool:
            render_endgame("win")

        # flip() the display to put your work on screen.
        pygame.display.flip()

        dt = clock.tick(60) / 1000


    pygame.quit()

except Exception as e:
    print(e)