from servo import Servo
from time import sleep

servo = Servo(pin=0)

while True:
    try:
        angle = int(input("Please enter the servo angle (0-180, or 'q' to quit): "))
        if angle < 0 or angle > 180:
            print("Enter a value between 0-180")
        else:
            servo.move(angle)
    except ValueError:
        user_input = input("Invalid input. Did you mean to quit? (y/n): ")
        if user_input.lower() == 'y':
            break # Exit the loop
        else:
            print("Please enter an integer.")
    except KeyboardInterrupt:
        print("\nExiting...")
        break

# Optional: Return servo to a default position on exit
# servo.move(90)  # Example: move to the center