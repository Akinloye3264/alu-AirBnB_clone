#!/usr/bin/python3
"""Defines the entry point of the command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project."""
    prompt = "(hbnb) "
    __all_classes = {
        "BaseModel"
    }

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")  # newline before exiting
        return True

    # -----------------------------
    # CREATE
    # -----------------------------
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)

    # -----------------------------
    # SHOW
    # -----------------------------
    def do_show(self, args):
        """Show string representation of an instance based on class name and id."""
        arg_list = shlex.split(args)
        objects = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    # -----------------------------
    # DESTROY
    # -----------------------------
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        arg_list = shlex.split(args)
        objects = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    # -----------------------------
    # ALL
    # -----------------------------
    def do_all(self, args):
        """Prints all string representations of instances."""
        arg_list = shlex.split(args)
        objects = storage.all()
        obj_list = []
        if len(arg_list) == 0:
            for obj in objects.values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        if arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        for key, obj in objects.items():
            if key.startswith(arg_list[0] + "."):
                obj_list.append(str(obj))
        print(obj_list)

    # -----------------------------
    # UPDATE
    # -----------------------------
    def do_update(self, args):
        """Updates an instance by adding or updating attribute."""
        arg_list = shlex.split(args)
        objects = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in objects:
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return
        obj = objects[key]
        attr_name = arg_list[2]
        attr_value = arg_list[3]
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
