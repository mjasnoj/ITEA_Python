>>> import xml.etree.ElementTree as ET
>>> root = ET.Element('days')
>>> day = ET.SubElement(root, 'day')
>>> day.set('date', '01.01.2017')
>>> task = ET.SubElement(day, 'WakeUp')
>>> task1 = ET.SubElement(day, 'task')
>>> task1.text = 'WakeUp'
>>> task2 = ET.SubElement(day, 'task')
>>> task2.text = 'MakeUp'
>>>
>>> tree = ET.ElementTree(root)
>>> tree.write('example/tasks.xml')



>>> doc = ET.parse('example/tasks.xml')
>>> print doc
<xml.etree.ElementTree.ElementTree object at 0x7f3b07c6bf10>
>>> root = doc.getroot()
>>> root.tag
'days'
>>> doc.findall('.//task')
[<Element 'task' at 0x7f3b07c79950>, <Element 'task' at 0x7f3b07c79990>]
>>> doc.findall('.//task')[0].text
'WakeUp'

>>> for task in doc.findall('.//task'):
...     print task
...
<Element 'task' at 0x7f3b07c79950>
<Element 'task' at 0x7f3b07c79990>
>>> for task in doc.findall('.//task'):
...     print task.text
...
WakeUp
MakeUp




1. DOM  - требует отпарсить весь документ в память. => высокая скорость доступа к данным; но: консистентсность данных + размер в памяти
2. StAX - проходит по документу последовательно, тег за тегом. Выгодно использовать при большом объеме и значении в середине документа
3. SAX


>>> from xml.dom import minidom
>>> doc = minidom.parse('example/tasks.xml')
>>> doc
<xml.dom.minidom.Document instance at 0x7f3b060cea28>
>>> doc.childNodes
[<DOM Element: days at 0x7f3b060ceab8>]
>>> doc.childNodes
[<DOM Element: days at 0x7f3b060ceab8>]
>>> doc.childNodes[0].tagName
u'days'
>>> doc.getElementsByTagName('task')
[<DOM Element: task at 0x7f3b060ced40>, <DOM Element: task at 0x7f3b060cee18>]
>>> doc.getElementsByTagName('task')[0].toxml()
u'<task>WakeUp</task>'
>>> doc.getElementsByTagName('task')[0].firstChild.toxml()
u'WakeUp'



>>> from xml.dom import pulldom
>>> doc = pulldom('example/tasks.xml')
>>> doc = pulldom.parse('example/tasks.xml')

>>> for event, node in doc:
...     if event == pulldom.START_ELEMENT and node.tag == 'task':
...             dic.expandNode(node)
...     if event == pulldom.START_ELEMENT and node.tagName == 'task':
...             dic.expandNode(node)
...             print node.toxml()

>>> for event, node in doc:
...     if event == pulldom.START_ELEMENT and node.tagName == 'task':
...             doc.expandNode(node)
...             print node.toxml()
...
<task>MakeUp</task>


>>> from xml import sax
>>> class MyHandler(sax.ContentHandler):
...     def startElement(self, name, attrs):
...             if name == 'task':
...                     self.task = True
...     def characters(self, content):
...             if self.task:
...                     print content
...     def endElement(self, name):
...             if name == 'task':
...                     self.task = False
...     def __init__(self):
...             self.task = False
...
>>> parser = sax.make_parser()
>>> parser.setContentHandler(MyHandler)
>>> parser.setContentHandler(MyHandler())
>>> parser.parse(open('example/tasks.xml', 'r'))
WakeUp
MakeUp
