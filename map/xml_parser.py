from xml.sax import *
from xml.dom.minidom import Document, parse
import xml.dom.minidom
import os
import datetime
from panel.panel_map import MapNode, MapInfo, MapRope, MapPortal
import operator


class XmlParser:
    def __init__(self):
        super(XmlParser, self).__init__()

    def parse_file(self, file_name):
        try:
            dom_tree = xml.dom.minidom.parse(file_name)
            elements = dom_tree.documentElement
            trs = elements.getElementsByTagName("tr")
            map_node = None
            map_rope = None
            map_portal = None
            map_nodes = []
            map_ropes = []
            map_portals = []
            curr_map = MapInfo()
            curr_map.map_nodes = map_nodes
            curr_map.map_ropes = map_ropes
            curr_map.map_portals = map_portals
            for tr in trs:
                td1 = tr.childNodes[0]
                td2 = tr.childNodes[1]

                text1 = self.get_text(td1)
                text2 = self.get_text(td2)
                if text1 is not None:
                    # 落脚点
                    if text1.find("foothold") != -1:
                        if text1.find(".x1") != -1:
                            map_node = MapNode()
                            map_nodes.append(map_node)
                            map_node.x1 = float(text2)
                            map_node.index = self.get_index(text1)
                        elif text1.find(".y1") != -1:
                            map_node.y1 = float(text2)
                        elif text1.find(".x2") != -1:
                            map_node.x2 = float(text2)
                        elif text1.find(".y2") != -1:
                            map_node.y2 = float(text2)
                        elif text1.find(".prev") != -1:
                            map_node.prev = int(text2)
                        elif text1.find(".next") != -1:
                            map_node.next = int(text2)
                        elif text1.find(".forbidFallDown") != -1:
                            map_node.forbid_fall_down = int(text2)
                    # 中心点
                    elif text1.find(".centerX") != -1:
                        curr_map.center_x = float(text2)
                    elif text1.find(".centerY") != -1:
                        curr_map.center_y = float(text2)
                    # 梯子
                    elif text1.find("ladderRope") != -1:
                        if text1.find(".x") != -1:
                            map_rope = MapRope()
                            map_ropes.append(map_rope)
                            map_rope.x = float(text2)
                            map_rope.index = self.get_index(text1)
                        elif text1.find(".y1") != -1:
                            map_rope.y1 = float(text2)
                        elif text1.find(".y2") != -1:
                            map_rope.y2 = float(text2)

                    # 传送点
                    elif text1.find("portal") != -1:
                        if text1.find(".x") != -1:
                            map_portal = MapPortal()
                            map_portals.append(map_portal)
                            map_portal.x = float(text2)
                            map_portal.index = self.get_index(text1)
                        elif text1.find(".y") != -1:
                            map_portal.y = float(text2)
                        elif text1.find(".tm") != -1:
                            map_portal.tm = int(text2)

            # sort_index = operator.attrgetter('next')
            # map_nodes.sort(key=sort_index)
            return curr_map
        except Exception as e:
            print(e)

    def get_text(self, node):
        for text_node in node.childNodes:
            if text_node.nodeType == node.TEXT_NODE:
                return text_node.data
        return None

    def get_index(self, node_text):
        node_arr = node_text.split(".")
        return int(node_arr[len(node_arr) - 2])
