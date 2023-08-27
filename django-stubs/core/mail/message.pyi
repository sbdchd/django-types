from collections.abc import Sequence
from email._policybase import Policy  # type: ignore
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, overload

utf8_charset: Any
utf8_charset_qp: Any
DEFAULT_ATTACHMENT_MIME_TYPE: str
RFC5322_EMAIL_LINE_LENGTH_LIMIT: int

class BadHeaderError(ValueError): ...

ADDRESS_HEADERS: Any

def forbid_multi_line_headers(
    name: str, val: str, encoding: str
) -> tuple[str, str]: ...
def split_addr(addr: str, encoding: str) -> tuple[str, str]: ...
def sanitize_address(addr: tuple[str, str] | str, encoding: str) -> str: ...

class MIMEMixin: ...

class SafeMIMEMessage(MIMEMixin, MIMEMessage):
    defects: list[Any]
    epilogue: None
    policy: Policy  # type: ignore [no-any-unimported]
    preamble: None

class SafeMIMEText(MIMEMixin, MIMEText):
    defects: list[Any]
    epilogue: None
    policy: Policy  # type: ignore [no-any-unimported]
    preamble: None
    encoding: str = ...
    def __init__(
        self, _text: str, _subtype: str = ..., _charset: str = ...
    ) -> None: ...

class SafeMIMEMultipart(MIMEMixin, MIMEMultipart):
    defects: list[Any]
    epilogue: None
    policy: Policy  # type: ignore [no-any-unimported]
    preamble: None
    encoding: str = ...
    def __init__(
        self,
        _subtype: str = ...,
        boundary: None = ...,
        _subparts: None = ...,
        encoding: str = ...,
        **_params: Any
    ) -> None: ...

_AttachmentContent = bytes | EmailMessage | Message | SafeMIMEText | str
_AttachmentTuple = (
    tuple[str, _AttachmentContent]
    | tuple[str | None, _AttachmentContent, str]
    | tuple[str, _AttachmentContent, None]
)

class EmailMessage:
    content_subtype: str = ...
    mixed_subtype: str = ...
    encoding: Any = ...
    to: list[str] = ...
    cc: list[Any] = ...
    bcc: list[Any] = ...
    reply_to: list[Any] = ...
    from_email: str = ...
    subject: str = ...
    body: str = ...
    attachments: list[Any] = ...
    extra_headers: dict[Any, Any] = ...
    connection: Any = ...
    def __init__(
        self,
        subject: str = ...,
        body: str | None = ...,
        from_email: str | None = ...,
        to: Sequence[str] | None = ...,
        bcc: Sequence[str] | None = ...,
        connection: Any | None = ...,
        attachments: Sequence[MIMEBase | _AttachmentTuple] | None = ...,
        headers: dict[str, str] | None = ...,
        cc: Sequence[str] | None = ...,
        reply_to: Sequence[str] | None = ...,
    ) -> None: ...
    def get_connection(self, fail_silently: bool = ...) -> Any: ...
    # TODO: when typeshed gets more types for email.Message, move it to MIMEMessage, now it has too many false-positives
    def message(self) -> Any: ...
    def recipients(self) -> list[str]: ...
    def send(self, fail_silently: bool = ...) -> int: ...
    @overload
    def attach(self, filename: MIMEText = ...) -> None: ...
    @overload
    def attach(
        self,
        filename: None = ...,
        content: _AttachmentContent = ...,
        mimetype: str = ...,
    ) -> None: ...
    @overload
    def attach(
        self,
        filename: str = ...,
        content: _AttachmentContent = ...,
        mimetype: str | None = ...,
    ) -> None: ...
    def attach_file(self, path: str, mimetype: str | None = ...) -> None: ...

class EmailMultiAlternatives(EmailMessage):
    alternative_subtype: str = ...
    alternatives: Sequence[tuple[_AttachmentContent, str]] = ...
    def __init__(
        self,
        subject: str = ...,
        body: str = ...,
        from_email: str | None = ...,
        to: Sequence[str] | None = ...,
        bcc: Sequence[str] | None = ...,
        connection: Any | None = ...,
        attachments: Sequence[MIMEBase | _AttachmentTuple] | None = ...,
        headers: dict[str, str] | None = ...,
        alternatives: Sequence[tuple[_AttachmentContent, str]] | None = ...,
        cc: Sequence[str] | None = ...,
        reply_to: Sequence[str] | None = ...,
    ) -> None: ...
    def attach_alternative(
        self, content: _AttachmentContent, mimetype: str
    ) -> None: ...
