from xml.sax import *
from xml.dom.minidom import Document, parse
import xml.dom.minidom
import os
import datetime
from panel.panel_map import MapNode, MapInfo


class XmlParser:
    def __init__(self):
        super(XmlParser, self).__init__()

    def parse_file(self, file_name):
        try:
            dom_tree = xml.dom.minidom.parse(file_name)
            elements = dom_tree.documentElement
            trs = elements.getElementsByTagName("tr")
            map_node = None
            map_nodes = []
            curr_map = MapInfo()
            curr_map.map_nodes = map_nodes
            for tr in trs:
                td1 = tr.childNodes[0]
                td2 = tr.childNodes[1]

                text1 = self.get_text(td1)
                text2 = self.get_text(td2)
                if text1 is not None:
                    if text1.find(".x1") != -1:
                        map_node = MapNode()
                        map_nodes.append(map_node)
                        map_node.x1 = float(text2)
                    elif text1.find(".x2") != -1:
                        map_node.x2 = float(text2)
                    elif text1.find(".y1") != -1:
                        map_node.y1 = float(text2)
                    elif text1.find(".y2") != -1:
                        map_node.y2 = float(text2)
                    elif text1.find(".prev") != -1:
                        map_node.prev = float(text2)
                    elif text1.find(".next") != -1:
                        map_node.next = float(text2)
                    elif text1.find(".forbid_fall_down") != -1:
                        map_node.forbid_fall_down = int(text2)
                    elif text1.find(".centerX") != -1:
                        curr_map.center_x = float(text2)
                    elif text1.find(".centerY") != -1:
                        curr_map.center_y = float(text2)

            return curr_map
        except Exception as e:
            print(e)

    def get_text(self, node):
        for text_node in node.childNodes:
            if text_node.nodeType == node.TEXT_NODE:
                return text_node.data
        return None
