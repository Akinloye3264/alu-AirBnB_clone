# console.py example snippet
from models import storage
from models.user import User
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel, "User": User}

def do_create(cls_name):
    if cls_name in classes:
        obj = classes[cls_name]()
        obj.save()
        print(obj.id)
    else:
        print("** class doesn't exist **")

def do_show(cls_name, id):
    key = f"{cls_name}.{id}"
    all_objs = storage.all()
    if key in all_objs:
        print(all_objs[key])
    else:
        print("** no instance found **")

def do_destroy(cls_name, id):
    key = f"{cls_name}.{id}"
    all_objs = storage.all()
    if key in all_objs:
        del all_objs[key]
        storage.save()
    else:
        print("** no instance found **")

def do_all(cls_name=None):
    all_objs = storage.all(classes.get(cls_name, None))
    print([str(obj) for obj in all_objs.values()])
