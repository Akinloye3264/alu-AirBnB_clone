#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter for the HBNB project.
    """
    prompt = "(hbnb) "
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it to the JSON file,
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances based on the
        class name or not.
        """
        all_objs = storage.all()
        obj_list = []
        if not arg:
            for obj in all_objs.values():
                obj_list.append(str(obj))
            print(obj_list)
            return

        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        for obj in all_objs.values():
            if obj.__class__.__name__ == class_name:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute.
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attribute_name = args[2]
        attribute_value_str = args[3]
        try:
            attribute_value = eval(attribute_value_str)
        except (NameError, SyntaxError):
            attribute_value = attribute_value_str

        setattr(obj, attribute_name, attribute_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
