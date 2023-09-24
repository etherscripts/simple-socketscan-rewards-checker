# Coded by: https://t.me/CryptoResearchLab

import requests

socket_scan_endpoint = "https://loki.socket.tech/get-claim-data?address={}"


def check_address_for_rewards(address, endpoint):
    try:
        url = endpoint.format(address)
        response = requests.get(url)
        return response.json()
    except Exception as error:
        print(f"Возникла ошибка: {error}.")


def process_addresses(file_path):
    try:
        with open(file_path, 'r') as file:
            addresses = file.read().splitlines()

        for address in addresses:
            socket_scan_rewards = check_address_for_rewards(address, socket_scan_endpoint)

            claimable_amount = socket_scan_rewards['result']['claimableAmount']
            pending_amount = socket_scan_rewards['result']['pendingAmount']
            claimed_amount = socket_scan_rewards['result']['claimedAmount']

            print(f"{address} | Claimable: {claimable_amount} | Pending: {pending_amount} | Claimed: {claimed_amount}")
    except Exception as error:
        print(f"Возникла ошибка: {error}.")


if __name__ == "__main__":
    file_path = "addresses.txt"
    process_addresses(file_path)
