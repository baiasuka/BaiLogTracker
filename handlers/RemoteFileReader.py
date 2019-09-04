import paramiko

class FtpCilent:
    def __init__(self, host, port, username, password, timeout=5):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._timeout = timeout

    def __enter__(self):
        self._cilent = paramiko.SSHClient()
        self._cilent.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._cilent.connect(self._host, self._port, self._username, self._password)
        self._sftp_cilent = self._cilent.open_sftp()
        return self._sftp_cilent

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cilent.close()


if __name__ == '__main__':
    pass
