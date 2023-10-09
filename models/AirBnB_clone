#!/usr/bin/python3
"""program containing the entry point of the command interpreter:"""
import cmd
import sys
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """The command Interpreter class"""
    prompt = "(hbnb) "

    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, arg):
        """command to exit program"""
        return True

    def emptyline(self):
        """validates empty lines to ensure they do nothing"""
        pass

    def do_EOF(self, arg):
        """command to exit program"""
        return True

    def do_create(self, arg):
        """
        new instance of a class created and saved to Json file
        Usage: create <class name>
        """
        arg_list = shlex.split(arg)
        if len(arg_list) < 1:
            print("** class name missing **")
            return

        if (arg_list[0] in HBNBCommand.class_dict.keys()):
            obj = HBNBCommand.class_dict[arg_list[0]]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """string representation of an instance printed based on class name
        and id"""
        storage.reload()
        stored_obj = storage.all()
        arg_list = shlex.split(arg)

        if len(arg_list) < 1:
            print("** class name missing **")
            return

        if arg_list[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return

        key = arg_list[0] + "." + arg_list[1]
        try:
            stored_obj[key]
        except KeyError:
            print("** no instance found **")
            return
        print(str(stored_obj[key]))

    def do_destroy(self, arg):
        """an instance gets deleted based on the class name and id"""

        arg_list = shlex.split(arg)
        stored_obj = storage.all()

        if len(arg_list) < 1:
            print("** class name missing **")
            return

        if arg_list[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return

        key = arg_list[0] + "." + arg_list[1]
        try:
            stored_obj[key]
        except KeyError:
            print("** no instance found **")
            return
        del stored_obj[key]
        storage.save()

    def do_all(self, arg):
        """
        string representation of all instances printed
        based on class name.
        Ex: all BaseModel or all

        Usage:(1) all
              (2) all <class name>
        """
        storage.reload()
        obj_list = []
        objects = storage.all()
        if arg == "":
            for key, value in objects.items():
                obj_list.append(str(value))
            print(json.dumps(obj_list))
            return
        arg_list = shlex.split(arg)
        if (arg_list[0] not in HBNBCommand.class_dict.keys()):
            print("** class doesn't exist **")
            return
        for key, value in objects.items():
            if arg_list[0] in key:
                obj_list.append(str(value))
        print(json.dumps(obj_list))

    def do_count(self, arg):
        """ number of objects of a particular class instance are counted"""
        storage.reload()
        obj = storage.all()
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return

        count = 0
        for key in obj:
            if args[0] in key:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        an instance is updated based on the class name and id and
        the change is saved into the JSON file.
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com

        update <class name> <id> <attribute name> "<attribute value>"

        """
        arg_list = shlex.split(arg)
        arg_len = len(arg_list)
        if arg_len < 1:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return
        if arg_len == 1:
            print("** instance id missing **")
            return
        storage.reload()
        objects = storage.all()
        key = arg_list[0] + "." + arg_list[1]
        try:
            objects[key]
        except KeyError:
            print("** no instance found **")
            return
        if arg_len == 2:
            print("** attribute name missing **")
            return
        try:
            eval(arg_list[2])
        except NameError:
            if arg_len == 3:
                print("** value missing **")
                return
        obj_dict = objects[key].__dict__
        try:
            eval(arg_list[2])
        except NameError:
            if arg_list[2] in obj_dict.keys():
                obj_dict[arg_list[2]] = type(
                        obj_dict[arg_list[2]])(arg_list[3])
            else:
                try:
                    obj_dict[arg_list[2]] = int(arg_list[3])
                except ValueError:
                    obj_dict[arg_list[2]] = arg_list[3]
            storage.save()
            return
        if type(eval(arg_list[2])) == dict:
            dict_kwarg = eval(arg_list[2])
            for key in dict_kwarg:
                if key in obj_dict.keys():
                    obj_dict[key] = type(obj_dict[key])(dict_kwarg[key])
                else:
                    try:
                        obj_dict[key] = int(dict_kwarg[key])
                    except ValueError:
                        obj_dict[key] = dict_kwarg[key]
            storage.save()
            return

    def default(self, args):
        """action on objects defined by -
        <class name>.all() : all the objects of a specified class name are retrieved
        """
        cmd_dict = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }
        arg = args.strip()
        val = arg.split(".")
        if len(val) != 2:
            cmd.Cmd.default(self, args)
            return
        class_name = val[0]
        method_call = val[1].split("(")[0]
        var = ""
        try:
            var = val[1].split("(")[1][-2]
        except IndexError:
            pass
        if var == "}":
            try:
                a = val[1].split("(")[1][:-1].split("{")
                _id = a[0][1:-3]
                dict_obj = "{" + a[1]
                copy = _id + " " + "'" + dict_obj.replace("'", '"', -1) + "'"
                if method_call == "update":
                    cmd_dict[method_call](class_name + " " + copy)
                return
            except IndexError:
                pass
        elif method_call == "update" and len(val[1].split("(")[1][:-1]) > 1:
            params = val[1].split("(")[1][:-1].split(",")
            line = "".join(params)[:]
            cmd_dict[method_call](class_name + " " + line)
        elif len(val[1].split("(")[1][:-1]) > 1:
            if method_call in cmd_dict.keys():
                p = val[1].split("(")[1][:-1]
                cmd_dict[method_call](class_name + " " + p)
        else:
            if method_call in cmd_dict.keys():
                cmd_dict[method_call](class_name)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
