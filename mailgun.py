import requests
import json


def send(
    domain: str,
    apikey: str,
    sender: str,
    recipient: str,
    subject: str,
    template: str,
    variables: dict[str, str],
) -> requests.Response:
    '''
    Send an email based on a Mailgun template.

    Returns a requests.Response object.

    domain -- String - The mailgun domain name
    apikey -- String - Api key to access mailgun's api
    sender -- String - "name <name@domain.com>"
    to -- String - "name <name@domain.com>"
    subject -- String - Email subject
    template -- String - template slug
    variables -- Dictionary - variables used in the template
    '''
    return requests.post(
        f'https://api.mailgun.net/v3/{domain}/messages',
        auth=("api", apikey),
        data={
            'from': sender,
            'to': recipient,
            'subject': subject,
            'template': template,
            'h:X-Mailgun-Variables': json.dumps(variables)
        }
    )


def get_status(response: str) -> str:
    '''
    Returns either 'queued' or 'failed'
    '''
    if response.startswith('Queued'):
        return 'queued'
    return 'failed'
