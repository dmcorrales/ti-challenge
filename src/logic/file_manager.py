import json
import secrets
from datetime import datetime


def transform_dates(file):
    output_file = file
    filer_keys = ["claimDateTime", "fileDateTime", "receivedDateTime"]
    for key_element in filer_keys:
        output_file[key_element] = format_date(output_file.get(key_element))
    return output_file


def format_date(timestamp):
    return datetime.fromtimestamp(timestamp / 1e3).strftime("%Y-%m-%dT%H:%M:%S")


def read_json():
    f = open("../resources/data.json")
    file = f.read()
    file = json.loads(file)
    f.close()
    return file


def get_payee(payee):
    return payee.get("id")


def get_invoices(invoices):
    return [invoice for invoice in invoices if "583" in invoice]


def save_json(file):
    f = open("../resources/" + secrets.token_hex(nbytes=16) + ".json", "w")
    f.write(json.dumps(file))
    f.close()


if __name__ == '__main__':
    file = read_json()
    payee = file.get("payee", {})
    payeeId = get_payee(payee)
    print(payeeId)
    invoices = file.get("invoiceIds", [])
    list_invoices = get_invoices(invoices)
    print(list_invoices)
    new_keys_json = transform_dates(file)
    print(new_keys_json)
    save_json(new_keys_json)
