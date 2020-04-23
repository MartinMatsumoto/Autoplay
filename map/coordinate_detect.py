from map.mini_map import MiniMapRect


class CoordinateDetect:
    chara_color = '#ffdd44'

    def __init__(self):
        return

    def detect_character(self, img, mini_map_rect: MiniMapRect):
        if mini_map_rect is None:
            return
        for x in range(mini_map_rect.left, mini_map_rect.right):
            for y in range(mini_map_rect.top, mini_map_rect.bottom):
                if img.pixelColor(x, y).name() == self.chara_color \
                        and img.pixelColor(x, y + 1).name() == self.chara_color \
                        and img.pixelColor(x + 1, y).name() == self.chara_color \
                        and img.pixelColor(x + 1, y + 1).name() == self.chara_color:
                    print(x, y)
                    return
