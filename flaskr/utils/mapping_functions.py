from ..model.resource_types import GameResource
from ..model.resource_consts import *


def getResFromName(name) -> GameResource:
    if name == "brick":
        return GameResource(
            "Кирпичи",
            "Кирпичи",
            "images/resources/icons/icon_resource_bricks.png",
            brickDesc)
    elif name == "fabric":
        return GameResource(
            "Ткань",
            "Ткань",
            "images/resources/icons/icon_resource_fabric.png",
            fabrickDesc)
    elif name == "ale":
        return GameResource(
            "Эль",
            "Эль",
            "images/resources/icons/icon_resource_ale.png",
            fabrickDesc)
    elif name == "coats":
        return GameResource(
            "Плащи",
            "Плащи",
            "images/resources/icons/icon_resource_coats.png",
            fabrickDesc)
    elif name == "incense":
        return GameResource(
            "Благовония",
            "Благовония",
            "images/resources/icons/icon_resource_incense.png",
            fabrickDesc)
    elif name == "cosmetics":
        return GameResource(
            "Красители",
            "Красители",
            "images/resources/icons/icon_resource_cosmetics.png",
            fabrickDesc)
    elif name == "parts":
        return GameResource(
            "Запчасти",
            "Запчасти",
            "images/resources/icons/icon_resource_parts.png",
            fabrickDesc)
    elif name == "planks":
        return GameResource(
            "Доски",
            "Доски",
            "images/resources/icons/icon_resource_planks.png",
            fabrickDesc)
    elif name == "fire":
        return GameResource(
            "Эссенция Древнего Огня",
            "Эссенция Древнего Огня",
            "images/resources/icons/icon_resource_wildfire.png",
            fabrickDesc)
    elif name == "scrolls":
        return GameResource(
            "Свитки",
            "Свитки",
            "images/resources/icons/icon_resource_scrolls.png",
            fabrickDesc)
    elif name == "training":
        return GameResource(
            "Тренировочное снаряжение",
            "Тренировочное снаряжение",
            "images/resources/icons/icon_resource_training_gear.png",
            fabrickDesc)
    elif name == "wine":
        return GameResource(
            "Вино",
            "Вино",
            "images/resources/icons/icon_resource_wine.png",
            fabrickDesc)
    else:
        return None
