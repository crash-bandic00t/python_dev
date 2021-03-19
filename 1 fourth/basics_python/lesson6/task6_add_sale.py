import sys
import json


if len(sys.argv) > 1:
    with open('sales.txt', 'r') as add:
        update = add.readline().strip()
        print(update)
        # if update == '':
        #     update_summ = [sys.argv[1]]
        # else:
        #     update_summ = json.loads(update)
        #     update_summ.append(sys.argv[1])
        # add.write(json.dumps(update_summ))
else:
    print('Введите сумму продаж')

