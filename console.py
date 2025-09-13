#!/usr/bin/python3
"""
This module defines the HBNBCommand class, a command-line interpreter
for managing objects.
"""
import cmd
import sys
import os
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter for the AirBnB project.
    """
    prompt = '(hbnb) '
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classes = {
            "BaseModel": BaseModel,
            "User": User
        }

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()
        
        if key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()
        
        if key not in all_objects:
            print("** no instance found **")
            return
        
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances
        or a specific class.
        """
        args = arg.split()
        all_objects = storage.all()
        result_list = []

        if not args:
            for obj in all_objects.values():
                result_list.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            
            for key, obj in all_objects.items():
                if obj.__class__.__name__ == class_name:
                    result_list.append(str(obj))
        
        print(result_list)
            
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating an attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()
        
        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        instance = all_objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()
    
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
        Called when an empty line is entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
