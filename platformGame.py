import pgzrun

# Window settings
WIDTH = 535
HEIGHT = 1000

# Player variables
player = Rect((500, 900), (40, 40))
velocity_y = 0
gravity = 1.45
on_ground = False

# Platforms
platforms = [
Rect((0, 900), (535, 100)),
Rect((0, 800), (535, 10)),
Rect((0, 700), (535, 10)),
Rect((0, 600), (535, 10)),
Rect((0, 500), (535, 10)),
Rect((0, 400), (535, 10)),
Rect((0, 300), (535, 10)),
Rect((0, 200), (535, 10)),
Rect((0, 0), (535, 100))
]

# Collectibles
coins = [
Rect((250, 340), (50, 30)),
Rect((400, 260), (50, 30)),
Rect((200, 775), (50, 30)),
Rect((150, 650), (50, 30))
]
score = 0

# Hazards and goal
lavas = [ 
Rect((450, 701), (20, 200)),
Rect((250, 701), (200, 20)),
Rect((250, 501), (20, 200)),
Rect((310, 635), (300, 20)),
Rect((310, 435), (20, 200)),
Rect((60, 435), (250, 20)),
Rect((60, 200), (20, 250)),
Rect((60, 201), (300, 20)),
Rect((360, 0), (20, 220)),
]
goal = Rect((0, 0), (535, 100))
game_won = False




def draw():
    screen.clear()
    screen.fill("green")
    screen.draw.filled_rect(player, "blue")

    for platform in platforms:
        screen.draw.filled_rect(platform, "white")

    for coin in coins:
        screen.draw.filled_rect(coin, "chocolate4")

    screen.draw.text(f"Score: {score}", (10, 100), fontsize=30, color="white")

    for lava in lavas:
        screen.draw.filled_rect(lava, "red")

    screen.draw.filled_rect(goal, "white")

    if game_won:
        screen.clear()
        screen.draw.text("You Win!", center=(267.5, 500), fontsize=60, color="yellow")
        screen.draw.text(f"Score: {score}", center = (267.5, 600), fontsize = 30, color = "white")

def update():
    global velocity_y, on_ground
    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH
    global velocity_y

    velocity_y += gravity
    player.y += velocity_y

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    if keyboard.space and on_ground:
        velocity_y = -18   
        on_ground = False

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

    global score

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
    for lava in lavas[:]:
        if player.colliderect(lava):
            player.x = 500
            player.y = 900
            velocity_y = 0

    global game_won

    if player.colliderect(goal):
        game_won = True

pgzrun.go()