from enum import Enum

class ResourceType(Enum):
    Brick = "images/resources/icons/icon_resource_bricks.png"
    Fabric = "images/resources/icons/icon_resource_fabric.png"


class GameResource:
    name = ""
    titleName = ""
    imageUrl = ""
    description = ""

    def __init__(self, name, titleName, imageUrl, description):
        self.name = name
        self.titleName = titleName
        self.imageUrl = imageUrl
        self.description = description
