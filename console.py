#!/usr/bin/python3
"""Console Program"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter for HBNB project"""
    prompt = "(hbnb)"

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF comman to exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
