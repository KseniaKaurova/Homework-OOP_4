import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_server: str, file_path: str):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_server, 'overwrite': 'true'}
        response_1 = requests.get(upload_url, headers=headers, params=params)
        data = response_1.json()
        href = data.get('href')
        response = requests.put(href, data=open('C:\\Users\\КС\\Desktop\\Study\\Book\\Грокаем_алгоритмы.pdf', 'rb'))
        return response

if __name__ == '__main__':
    path_to_file = 'C:\\Users\\КС\\Desktop\\Study\\Book\\Грокаем_алгоритмы.pdf'
    token = 'y0_AgAAAAAnoTUgAADLWwAAAADnhlibXL4Zq6UyQMihIbHX_WUWs7OLLAw'
    uploader = YaUploader(token)
    result = uploader.upload('Грокаем_алгоритмы.pdf', path_to_file)