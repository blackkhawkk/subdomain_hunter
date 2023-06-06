import requests
import json

class SubdomainEnumerator:
    def __init__(self, domain, filepath, api_key):
        self.domain = domain
        self.filepath = filepath
        self.api_key = api_key

    def get_sub_domains(self):
        url = f"https://api.securitytrails.com/v1/domain/{self.domain}/subdomains"
        querystring = {"children_only": "true"}
        headers = {
            'accept': "application/json",
            'apikey': self.api_key
        }
        response = requests.get(url, headers=headers, params=querystring)
        result_json = json.loads(response.text)
        sub_domains = [i + '.' + self.domain for i in result_json['subdomains']]
        return sub_domains

    def save_sub_domains_to_file(self, sub_domains):
        with open(self.filepath, 'w+') as f:
            for sub_domain in sub_domains:
                f.write(sub_domain + '\n')

    def run(self):
        print("\nSubdomain Enumeration Script\n")
        sub_domains = self.get_sub_domains()
        self.save_sub_domains_to_file(sub_domains)


def main():
    domain = input("\nEnter Domain name: ")
    filepath = input("\nPlease provide a file name to save: ")
    api_key = input("\nEnter your API key: ")
    
    subdomain_enumerator = SubdomainEnumerator(domain, filepath, api_key)
    subdomain_enumerator.run()

if __name__ == '__main__':
    main()
