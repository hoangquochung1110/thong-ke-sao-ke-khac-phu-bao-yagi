import pdfplumber
from datetime import datetime
from saoke.models import Transaction
from django.db import transaction
import pytz


@transaction.atomic
def import_transactions(pages):
    transactions = []
    order = 0
    for page in pages:
        for line in page.extract_table():
            order, dt_str, comment, amount_str, offset_name = line
            date_obj = datetime.strptime(dt_str.strip(), "%m/%d/%Y\n%H:%M:%S").astimezone(
                tz=pytz.timezone("Asia/Ho_Chi_Minh")
            )
            amount = int(amount_str.replace('.', ''))

            print(f"{order=}, {date_obj=}, {comment=}, {amount=}, {offset_name=}")
            transaction = Transaction(
                order=order,
                transaction_datetime=date_obj,
                comment=comment,
                amount=amount,
                offset_name=offset_name,
            )
            transactions.append(transaction)


    Transaction.objects.bulk_create(transactions)


pdf = pdfplumber.open('./VietinBank CT1111 Support.pdf')

import_transactions(pdf.pages[1:])

