from xml.sax import *
from xml.dom.minidom import Document,parse
import xml.dom.minidom
import os
import datetime

class XmlParser():
    def __init__(self):
        super(XmlParser, self).__init__()

    def parse_file(self, file_name):
        try:
            # 使用minidom解析器打开 XML 文档
            DOMTree = xml.dom.minidom.parse(file_name)
            movies = DOMTree.documentElement
            # 在集合中获取所有电影
            movie_c = movies.getElementsByTagName("MOVIE")
            for movie in movie_c:
                try:
                    # print("*****Movie*****")
                    if movie.hasAttribute("YEAR"):
                        year = movie.getAttribute("YEAR")
                    if movie.hasAttribute("MINUTES"):
                        minutes = movie.getAttribute("MINUTES")
                    if movie.hasAttribute("ACQUIRED"):
                        ymd = movie.getAttribute("ACQUIRED").split("-")
                        if len(ymd) != 3:
                            raise ValueError("invalid acquired date {0}".format(
                                str(movie.getAttribute("ACQUIRED"))))
                        acquired = datetime.date(int(ymd[0]), int(ymd[1]),
                                                 int(ymd[2]))
                    title = notes = None
                    title_tag = movie.getElementsByTagName('TITLE')[0]
                    title = title_tag.childNodes[0].data
                    notes_tag = movie.getElementsByTagName('NOTES')[0]
                    print(title, year, minutes, acquired, notes)
                    try:
                        notes = notes_tag.childNodes[0].data
                    except Exception:
                        raise ValueError("missing title or notes")
                except ValueError as e:
                    print("Failed to import: {0}".format(e))
        except Exception as e:
            print(e)
