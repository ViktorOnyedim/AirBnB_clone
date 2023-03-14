#!/usr/bin/python3
"""Console Program"""
import cmd
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
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
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[arg]()
            obj.save()
            print(obj.id)

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
            obj_id = f"{cls_name}.{args[1]}"
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

    def help_destroy(self):
        """Help message for the destroy command"""
        print("Deletes an instance based on the class name and id")
        print("Saves it (to the JSON file) and prints the id")
        print("Usage: destroy <class_name> <id>")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        obj_list = []
        if not arg:
            obj_dict = models.storage.all()
            for obj in obj_dict.values():
                obj_list.append(str(obj))
        else:
            cls_name = arg.split()[0]
            if cls_name not in storage.classes():
                print("** class doesn't exist **")
                return
            obj_dict = models.storage.all()
            for key, obj in obj_dict.items():
                if obj.__class__.__name__ == cls_name:
                    obj_list.append(str(obj))
        print(obj_list)

        def do_update(self, arg):
            """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file)
            """
            args = arg.split()
            if not arg:
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
                obj_dict = storage.all()
                obj_id = args[1]
                key = f"{cls_name}.{obj_id}"
                if key not in obj_dict:
                    print("** no instance found **")
                    return
                obj = obj_dict[obj_id]
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                elif len(args) < 4:
                    print("** value missing **")
                    return
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    try:
                        attr_value = int(attr_value)
                    except ValueError:
                        try:
                            attr_value = float(attr_value)
                        except ValueError:
                            pass
                    setattr(obj, attr_name, attr_value)
                    obj.save()

        def help_update(self):
            """Help message for the update command"""
            print("Updates an instance based on the class name and id")
            print("by adding or updating attribute")
            print("Usage: ", end="")
            print("update <class name> <id> <attribute name> ", end="")
            print("\"<attribute value>\"")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
