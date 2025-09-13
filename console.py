#!/usr/bin/python3
"""Defines the entry point of the AirBnB command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")  # print newline before exiting
        return True

    def help_quit(self):
        """Help message for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command."""
        print("EOF signal to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
