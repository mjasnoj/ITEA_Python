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




1. DOM
2. StAX
3. SAX
