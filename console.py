#!/usr/bin/python3
"""Console Program"""
import cmd
import json
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """Command Interpreter for HBNB project"""
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF comman to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def help_quit(self):
        """Help message for the quit command"""
        print("Exit the command interpreter")

    def help_EOF(self):
        """Help message for the EOF command"""
        print("Exit the command interpreter")

    def do_create(self, arg):
        """Create a new instance of a BaseModel subclass."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                cls = models.getattr(models, arg)
                obj = cls()
                obj.save()
                print(obj.id)
            except AttributeError:
                print("** class doesn't exist **")

    def help_create(self):
        """Help message for the create command"""
        print("Create a new instance of BaseModel")
        print("Usage: create <class_name>")

    def show(self, arg):
        """S"""
        if not arg:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
