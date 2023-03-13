#!/usr/bin/python3
"""Console Program"""
import cmd
import json
from models.engine.file_storage import FileStorage
from models import storage
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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        else:
            cls_name = args[0]
            if cls_name not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_dict = models.storage.all()
            obj_id = f"{class_name}.{args[1]}"
            if obj_id not in obj_dict:
                print("** no instance found **")
                return
            else:
                obj = obj_dict[obj_id]
                print(obj)

    def help_show(self):
        """Help message for the show command"""
        print("Prints the string representation of an instance")
        print("Usage: show <class_name> <id>")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the changes into the JSON file)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        else:
            cls_name = args[0]
            if cls_name not in storage.classes():
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = f"{cls_name}.{obj_id}"
            obj_dict = models.storage.all()
            if key not in obj_dict:
                print("** no instance found **")
                return
            obj_dict.pop(key)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
