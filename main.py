import requests


class YaDiskManager:
    def __init__(self, token):
        self.token = token

    def upload_file(self, file_path, filename):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': 'False'}
        resp = requests.get(upload_url, headers=headers, params=params)
        href = resp.json().get('href')
        if href:
            resp = requests.put(href, data=open(filename, 'rb'))
            status = resp.status_code
        else:
            status = 'Fail'
        return status
    
    def resource_list(self, path):
        query_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': path, 'fields': '_embedded.items.name, _embedded.items.type'}
        resp = requests.get(query_url, headers=headers, params=params)
        if resp.status_code == 200:
            resource_list = resp.json()['_embedded']['items']
            return resource_list
        
    def create_folder(self, path):
        query_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': path}
        resp = requests.put(query_url, headers=headers, params=params)
        return resp.status_code
    
    def delete_folder(self, path):
        query_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': path}
        resp = requests.delete(query_url, headers=headers, params=params)
        return resp.status_code
