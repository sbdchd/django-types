from typing import Optional
from xml.sax.saxutils import XMLGenerator

class UnserializableContentError(ValueError): ...

class SimplerXMLGenerator(XMLGenerator):
    def addQuickElement(
        self,
        name: str,
        contents: Optional[str] = ...,
        attrs: Optional[dict[str, str]] = ...,
    ) -> None: ...
    def characters(self, content: str) -> None: ...
    def startElement(self, name: str, attrs: dict[str, str]) -> None: ...
