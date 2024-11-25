# Joshua Martin CIS261 Week 8 Lab Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

# Method to calculate the perimeter of the rectangle
    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

# Method to calculate the area of the rectangle
    def calculate_area(self):
        return self.height * self.width

# Method to print the rectangle dimensions
    def print_rectangle(self):
        print(f"\nRectangle with Height: {self.height} and Width: {self.width}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")

# Method to draw the outline of the rectangle using '*' character
    def draw_rectangle(self):
        print("\nDrawing the Rectangle Outline: ")
# Loop to draw the rectangle outline
        for i in range(int(self.height)):
            if i == 0 or i == int(self.height) - 1:
# Print top and bottom edges (full width of stars)
                print('*' * int(self.width))
            else:
# Print middle rows (only sides with spaces in between)
                print('*' + ' ' * (int(self.width) - 2) + '*')

# Function to prompt for height and width and create a rectangle object
def create_rectangle():
    while True:
        try:
            height = float(input("Enter a height for the rectangle: "))
            width = float(input("Enter a width for the rectangle: "))
            if height < 2 or width < 2:
                print("Height and width should be at least 2 to draw the outline.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for height and width.")
    
    rectangle = Rectangle(height, width)
    return rectangle

# Main function to run the program
def main():
    while True:
# Create a new rectangle and calculate its properties
        rectangle = create_rectangle()
        rectangle.print_rectangle()
        rectangle.draw_rectangle()  # Draw the rectangle outline

# Ask if the user wants to continue
        continue_choice = input("\nWould you like to calculate another rectangle? (y/n): ").lower()
        if continue_choice == 'n':
            print("Exiting the program.")
            break
        elif continue_choice != 'y':
            print("Invalid input, exiting the program.")
            break

# Run the program
if __name__ == "__main__":
    main()