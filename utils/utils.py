import json
from colorama import Fore

def get_operations():
    with open('operations.json') as json_file:
        finance_operations = json.load(json_file)

        operations = []
        count = 0
        for transaction in finance_operations:
            if count >= 5:
                break
            if transaction["state"] == "EXECUTED":
                operations.append(transaction)
                count += 1
    return operations

def get_date(op):
    return op['date']

def sorted_date(operations):
    sorted_operations = sorted(operations, key=get_date, reverse=True)
    operat = []
    for op in sorted_operations:
        operat.append(op)
    return operat


def main():
    operations = get_operations()
    sorted_operations = sorted_date(operations)


    for op in sorted_operations:
        date_ = op["date"][:10]
        right_date = Fore.RED + date_[-2:] + "." + "0" + date_[6:7] + "." + Fore.RESET +date_[:4]
        type_transaction = op["description"]


        if op.get("from") is not None:
            finance_comp = op["from"]
            masked_fin_comp = finance_comp[:-10] + "*" * 6 + finance_comp[-4:]
        else:
            masked_fin_comp = ""

        bank_account = op["to"]
        masked_bank_account = "*" * 2 + bank_account[-4:]
        summa_rub = op["operationAmount"]["amount"]
        valuta = op["operationAmount"]["currency"]["name"]


        print(f"{Fore.RED}{right_date} {Fore.RESET}{type_transaction}\n"
              f"{masked_fin_comp} -> {masked_bank_account}\n"
              f"{Fore.RED}{summa_rub} {Fore.RESET}{valuta}")
        print()



if __name__ == '__main__':
    main()


