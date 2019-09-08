import json
from collections import namedtuple
import  namedtupled
stepProcessingItems:namedtupled
def __init__():
    print("starting the file processing")
    file_obj=open('./sample.json','r')

    json_object=  json.load(file_obj)


    # print(json_object['accounting'][0])
    # print(type(json_object['accounting']))

    # namedTupleConstructor = namedtuple('myNamedTuple', ' '.join(sorted(json_object.keys())))
    # nt= namedTupleConstructor(**json_object)
    # print(type(nt))
    stepProcessingItems = namedtupled.map(json_object)
    print(stepProcessingItems.accounting)
    # for item in list(stepProcessingItems.accounting)
    # print(item.lastName)

__init__()