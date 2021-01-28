from xml.dom.minidom import parse
import xml.dom.minidom

class BookingRecord:
    def __init__(self, xml_path=None, *arg, **kwargs):
        self.DOMTree = xml.dom.minidom.parse(xml_path)
        self.collection = self.DOMTree.documentElement
        self.xml_path = xml_path
    def setText(self, doc, node, text):
        textnode = doc.createTextNode(text)
        node.appendChild(textnode)
    def createChild(self, name=None, email=None, phone=None, date=None, time=None,people=None, message=None):
        items = {'name':name, 'email':email, 'phone':phone, 'date':date, 'time':time, 'people':people, 'message':message}
        data = self.DOMTree.createElement('Booking')
        data.setAttribute('title', 'Table')
        for item in items:
            sub_element = self.DOMTree.createElement(item)
            self.setText(self.DOMTree, sub_element, items[item])
            data.appendChild(sub_element)
            self.collection.appendChild(data)
    def saveToXML(self):
        with open(self.xml_path, 'w') as output:
         output.write(self.DOMTree.toprettyxml())


class ContactRecord:
    def __init__(self, xml_path=None, *arg, **kwargs):
        self.DOMTree = xml.dom.minidom.parse(xml_path)
        self.collection = self.DOMTree.documentElement
        self.xml_path = xml_path

    def setText(self, doc, node, text):
        textnode = doc.createTextNode(text)
        node.appendChild(textnode)

    def createChild(self, name=None, email=None, subject=None, message=None):
        items = {'name':name, 'email':email, 'subject':subject, 'message':message}
        data = self.DOMTree.createElement('Contact')
        data.setAttribute('title', 'Customer Message')
        for item in items:
            sub_element = self.DOMTree.createElement(item)
            self.setText(self.DOMTree, sub_element, items[item])
            data.appendChild(sub_element)
            self.collection.appendChild(data)

    def saveToXML(self):
        with open(self.xml_path, 'w') as output:
            output.write(self.DOMTree.toprettyxml())