from sys import argv

#class DuplicatedValueException(Exception):
#    pass

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_arguments(default_arguments={}):
    for index,argument in enumerate(argv):
        if index==0:
            continue
        splitted=argument.split('=')
        if len(splitted)==1:
            default_arguments[argument]=True
        else:
            key=splitted[0]
            value=splitted[1]
            #if key in default_arguments:
            #    raise DuplicatedValueException('Key "{key}" already have a value "{value}" set'.format(key=key,value=default_arguments[key]))
            if value=='true' or value =='True':
                default_arguments[key]=True
            elif value=='false' or value =='False':
                default_arguments[key]=False
            elif is_float(value):
                default_arguments[key]=float(value)
            else:
                default_arguments[key]=value
    return default_arguments

if __name__=='__main__':
    arguments=get_arguments()
    print(arguments)