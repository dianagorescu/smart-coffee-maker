This is a simple command-line controlled coffee maker implemented in Python. It allows users to interact with the coffee maker by entering commands through the terminal.
Installation

To run the script, you need to have Python installed on your system. This script is compatible with both Python 2 and Python 3.
How to Use
Clone this repository to your local machine.

    git clone https://github.com/dianagorescu/smart-coffee-maker.git

Run the script.

    python3 coffee_maker.py


Commands

    list: Lists available coffee types.
    make: Makes a coffee. You will be prompted to choose the type of coffee.
    status: Checks the status of the resources (water, coffee, milk).
    refill: Refills the specified resource or all resources to 100%.
    help: Displays information about available commands.
    exit: Exits the coffee maker.

Available Coffee Types 

    Espresso
    Americano
    Cappuccino

Resources

    Water: Available resources for making coffee.
    Coffee: Available resources for making coffee.
    Milk: Available resources for making coffee.

Additional Notes

    When making coffee, the script checks if there are enough resources available.
    Coffee recipes are stored in separate files within the recipes/ folder.
