import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(title: str, content: str) -> str:
        pass


class JSONSerializer(Serializer):
    @staticmethod
    def serialize(title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(Serializer):
    @staticmethod
    def serialize(title: str, content: str) -> str:
        root = ET.Element("book")
        root_title = ET.SubElement(root, "title")
        root_title.text = title
        root_content = ET.SubElement(root, "content")
        root_content.text = content
        return ET.tostring(root, encoding="unicode")


class SerializeMixin:
    __SERIALIZE_TYPES = {
        "json": JSONSerializer,
        "xml": XMLSerializer,
    }

    def serialize(self, serialize_type: str) -> str:
        serializer = self.__SERIALIZE_TYPES.get(serialize_type)
        if serializer:
            return serializer.serialize(self.title, self.content)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
