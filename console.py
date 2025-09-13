#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

# dictionary of available classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()  # instantiate the right class
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances, or all instances of a class"""
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif arg in classes:
            print([str(obj) for key, obj in objs.items() if key.startswith(arg + ".")])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value**
