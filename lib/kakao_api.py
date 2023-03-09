import requests

url = 'https://dapi.kakao.com/v2/local/search/address.json'
params = {
    'analyze_type': 'similar',
    'page': 1,
    'size': 10,
}


class KakaoApi:
    def __init__(self, token):
        self.headers = {
            'Authorization': f'KakaoAK {token}'
        }

    def find_coordinate(self, address):
        response = requests.get(
            url,
            params={**params, 'query': address},
            headers=self.headers,
        ).json()

        try:
            documents = response.get('documents')
            document = documents[0]
            address = document.get('address')
            x, y = address.get('x'), address.get('y')

            return x, y
        except (NameError, IndexError, AttributeError):
            return None, None
