# Email Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

DEFAULT_EMAIL = "support@marckcode.com"
LOGIN = "admin"
PASSWORD = "admin"

class EmailClient:
    def __init__(
        self,
        login: str | None = None,
        password: str | None = None,
        name: str | None = None,
        to_address: str = DEFAULT_EMAIL,
    ):
        self._server = SMTP()
        host, port = str(self._server._host).split(":") # type: ignore
        self._host: str = host
        self._port - int(port)
        
        if not login or not password:
            self._login, self._password = LOGIN, PASSWORD
        else:
            self._login, self._password = login, password
            
        self.name = name
        self.to_addres = to_address
        
    def _connect(self) -> None:
        self._server.connect(self._host, self._port)
        self._server.starttls()
        self._server.login(self._login, self._password)
        
    def _quit(self) -> None:
        self._server.quit()
        
    def send_message(
        self,
        from_address: str,
        to_address: str,
        subject: str = "Non subject",
        message: str = "",
    ) -> None:
        msg = MIMEMultipart()
        msg["From"] = from_address
        if not to_address:
            to_address = self.to_addres
            
        msg["To"] = to_address
        msg["Subject"] = subject
        mime = MIMEText(
            message,
            "html" if message.lower().startswith("<!doctype html>") else ""
        )
        msg.attach(mime)

