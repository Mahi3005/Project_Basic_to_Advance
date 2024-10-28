import turtle
import time
import random

# Constants
WIDTH, HEIGHT = 800, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def draw_background():
    """Draw a beautiful background with grass and sky"""
    bg = turtle.Turtle()
    bg.speed(0)
    bg.penup()
    bg.hideturtle()

    # Draw sky (simplified gradient)
    bg.goto(-WIDTH // 2, -HEIGHT // 2)
    colors = ['#87CEEB', '#ADD8E6', '#B0E0E6', '#87CEEB']
    section_height = HEIGHT // len(colors)

    for i, color in enumerate(colors):
        bg.goto(-WIDTH // 2, -HEIGHT // 2 + i * section_height)
        bg.pendown()
        bg.fillcolor(color)
        bg.begin_fill()
        for _ in range(4):
            bg.forward(WIDTH if _ % 2 == 0 else section_height)
            bg.left(90)
        bg.end_fill()
        bg.penup()

    # Draw grass
    bg.goto(-WIDTH // 2, -HEIGHT // 2)
    bg.pendown()
    bg.fillcolor('#90EE90')
    bg.begin_fill()
    bg.goto(WIDTH // 2, -HEIGHT // 2)
    bg.goto(WIDTH // 2, -HEIGHT // 2 + 100)
    bg.goto(-WIDTH // 2, -HEIGHT // 2 + 100)
    bg.goto(-WIDTH // 2, -HEIGHT // 2)
    bg.end_fill()


def draw_lanes(colors):
    """Draw race lanes"""
    spacing_x = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        # Draw lane
        lane_marker = turtle.Turtle()
        lane_marker.speed(0)
        lane_marker.penup()
        lane_marker.goto(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 30)
        lane_marker.pendown()
        lane_marker.hideturtle()
        lane_marker.color(color)
        lane_marker.pensize(2)
        lane_marker.setheading(90)

        # Draw dotted line
        for _ in range(20):
            lane_marker.forward(15)
            lane_marker.penup()
            lane_marker.forward(15)
            lane_marker.pendown()


def draw_title():
    """Draw a fancy title"""
    title = turtle.Turtle()
    title.speed(0)
    title.penup()
    title.hideturtle()
    title.goto(0, HEIGHT // 2 - 80)
    title.color('red')
    title.write("🏁 TURTLE RACE 🏁", align="center",
                font=("Arial", 32, "bold"))


def draw_finish_line():
    """Draw a checkered finish line"""
    finish = turtle.Turtle()
    finish.speed(0)
    finish.penup()
    finish.hideturtle()

    square_size = 20
    y_pos = HEIGHT // 2 - 120
    for x in range(-WIDTH // 2, WIDTH // 2, square_size):
        finish.goto(x, y_pos)
        finish.fillcolor('black' if (x / square_size) % 2 == 0 else 'white')
        finish.pendown()
        finish.begin_fill()
        for _ in range(4):
            finish.forward(square_size)
            finish.right(90)
        finish.end_fill()
        finish.penup()


def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        # Create and setup racer
        racer = turtle.Turtle()
        racer.speed(0)
        racer.shape('turtle')
        racer.shapesize(1.5, 1.5)
        racer.fillcolor(color)
        racer.pencolor(color)
        racer.pensize(2)

        # Position racer
        racer.penup()
        racer.goto(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 50)
        racer.left(90)

        turtles.append(racer)

        # Starting animation
        for _ in range(3):
            racer.shapesize(1.7, 1.7)
            time.sleep(0.1)
            racer.shapesize(1.5, 1.5)
            time.sleep(0.1)

    return turtles


def display_winner(winner_color):
    """Display winner announcement with animation"""
    announcement = turtle.Turtle()
    announcement.speed(0)
    announcement.penup()
    announcement.hideturtle()
    announcement.goto(0, 0)

    text = f"🎉 {winner_color.upper()} TURTLE WINS! 🎉"
    announcement.color(winner_color)

    for size in range(20, 40, 4):
        announcement.clear()
        announcement.write(text, align="center",
                           font=("Arial", size, "bold"))
        time.sleep(0.1)


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            # Add motion effect
            racer.shapesize(1.4, 1.6)
            time.sleep(0.05)
            racer.shapesize(1.5, 1.5)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 130:
                winning_color = racer.fillcolor()
                display_winner(winning_color)
                return winning_color


def get_number_of_racers(screen):
    """Get number of racers using screen dialog"""
    while True:
        answer = screen.textinput("Number of Racers",
                                  "How many turtles would you like to race? (2-10)")
        if answer is None:  # If user closes dialog
            return 2  # Default to minimum racers

        if answer.isdigit():
            racers = int(answer)
            if 2 <= racers <= 10:
                return racers
            else:
                screen.textinput("Error", "Please enter a number between 2 and 10")
        else:
            screen.textinput("Error", "Please enter a valid number")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('🐢 Turtle Racing Championship 🏁')
    screen.bgcolor('#87CEEB')
    screen.tracer(0)

    draw_background()
    draw_title()
    draw_finish_line()

    screen.tracer(1)
    return screen


def main():
    screen = init_turtle()
    racers = get_number_of_racers(screen)

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    # Draw lanes before creating turtles
    draw_lanes(colors)

    winner = race(colors)

    screen.exitonclick()


if __name__ == "__main__":
    main()