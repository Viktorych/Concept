import ast
import json
class P_Size:
    """ Свойство размер"""
    prp_name="P_Size"
    width=0
    height=0
    def __init__(self):
        exec ('self.x=10')
        pass
    def __str__(self):
        return "Наименование свойства: {} Ширина:{} Высота:{}".format (self.prp_name,self.width,self.height)

    def setW (self, width):
        self.width=width

    def setH (self, height):
        self.height=height
    def formJson (self, jsonData):
        _obj = json.loads(jsonData)
        _size=_obj["P_Size"]
        #print (_size.items())
        self.width=_size["width"]
        self.height=_size ["height"]







dic={}
#dic.

json_data = '{"P_Size": {"width":50,"height":30}}'
object_data='{"id":"dddd","type":"коробка","name":"ящик","P_Size": {"width":10,"height":20},"P_Size": {"width":10,"height":30}}'
python_obj = json.loads(json_data)
s=P_Size()
s.formJson(json_data)
#s.setH(10)
#s.setW(20)
print (s)
print (python_obj.items())
print (python_obj["P_Size"].keys())