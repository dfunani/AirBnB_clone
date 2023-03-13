#!/usr/bin/python3
"""Console module
creates an instance of a command window
"""
import cmd
from models import storage
import importlib
import re
import json


class HBNBCommand(cmd.Cmd):
    """ Program Class window inheriting from the base CMD class """

    prompt = "(hbnb) "

    def default(self, arg):
        """ Handles line args """
        if arg.split('.')[0] not in storage.factory():
            return False
        if arg.split('.', 1)[-1] == 'all()':
            self.do_all(arg.split('.')[0])
            return False
        if arg.split('.', 1)[-1] == 'count()':
            count = 0
            for obj in dict(storage.all()):
                if arg.split('.')[0] == obj.split('.')[0]:
                    count += 1
            print(count)
            return False

        show = re.search(r'[.]show[(](.*)[)]', arg)
        if show:
            self.do_show((arg.split('.')[0] + ' ' + show.groups()[0]).strip())
            return False

        destroy = re.search(r'[.]destroy[(](.*)[)]', arg)
        if destroy:
            self.do_destroy((arg.split('.')[0] + ' ' +
                             destroy.groups()[0]).strip())
            return False

        dict_update = re.search(r"[.]update[(](.*)[,]?([{].*[}])[)]",
                                arg)
        if dict_update:
            try:
                storage.dict_update((arg.split('.')[0] + '.' +
                                     dict_update.groups()[0].replace(',', '')
                                     .strip()), json
                                    .loads(dict_update.groups()[1]))
                storage.save()
                storage.reload()
            except Exception as e:
                pass
            finally:
                return False

        update = re.search(r'[.]update[(](.*)[,]?(.*)[,]?(.*)[)]', arg)
        if update:
            self.do_update((arg.split('.')[0] + ' ' +
                            update.groups()[0].replace(',', '') + ' ' +
                            update.groups()[1].replace(',', '') + ' ' +
                            update.groups()[2]).strip())
            return False

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.factory():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, arg):
        """Update a BaseModel ID - Only one attribute permissible """
        if not arg:
            print("** class name missing **")
            return False
        if arg.split(' ')[0] not in storage.factory():
            print("** class doesn't exist **")
            return False
        if len(arg.split(" ")) < 2:
            print("** instance id missing **")
            return False
        else:
            for key in dict(storage.all()):
                if key == (arg.split(' ')[0] + '.' + arg.split(" ")[1]):
                    if len(arg.split(' ')) < 3:
                        print("** attribute name missing **")
                        return False
                    if len(arg.split(' ')) < 4:
                        print("** value missing **")
                        return False
                    storage.update(key, arg.split(' ')[2], arg.split(' ')[3])
                    storage.all()[key].save()
                    return False
            print("** no instance found **")
            return False

    def do_all(self, arg):
        """Shows all the BaseModels in storage """
        if arg and arg in storage.factory():
            res = []
            for key, obj in storage.all().items():
                if type(obj).__name__ == arg.split(' ')[0]:
                    res.append(str(obj))
            print(res)
            return False
        elif arg and arg.split(' ')[0] not in storage.factory():
            print("** class doesn't exist **")
            return False
        else:
            res = [str(val) for key, val in storage.all().items()]
            print(res)
            return False

    def do_destroy(self, arg):
        """Deletes a given BaseModel ID """
        if not arg:
            print("** class name missing **")
            return False
        if arg.split(" ")[0] not in storage.factory():
            print("** class doesn't exist **")
            return False
        if len(arg.split(" ")) < 2:
            print("** instance id missing **")
            return False
        for objs in storage.all():
            if objs == (arg.split(' ')[0] + '.' + arg.split(" ")[1]):
                storage.delete(objs)
                storage.save()
                return False
        print("** no instance found **")
        return False

    def do_show(self, arg):
        """Shows one particlar BaseModel ID """
        if not arg:
            print("** class name missing **")
            return False
        if arg.split(' ')[0] not in storage.factory():
            print("** class doesn't exist **")
            return False
        if len(arg.split(" ")) < 2:
            print("** instance id missing **")
            return False
        for objs in storage.all():
            if objs == (arg.split(' ')[0] + '.' + arg.split(" ")[1]):
                print(storage.all()[objs])
                return False
        print("** no instance found **")
        return False

    def do_create(self, arg):
        """Creates a new Basemodel Class to storage """
        if not arg:
            print("** class name missing **")
            return False
        if arg not in storage.factory():
            print("** class doesn't exist **")
            return False
        bm = storage.factory()[arg]()
        bm.save()
        print(bm.id)
        return False

    def emptyline(self):
        """Overrides emptyline - nothing happens when no command is given """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program\n """
        return True

    def do_EOF(self, arg):
        """Handler for the end of File/Program """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
