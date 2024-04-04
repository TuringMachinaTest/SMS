from .models import Account


def get_partitions_choices(account_id = -1):
    if account_id == -1:
        return ()
    else:
        account = Account.objects.get(pk=account_id)
        
        return (
            (0  , "0 : " + account.partition_name0),
            (1  , "1 : " + account.partition_name1),
            (2  , "2 : " + account.partition_name2),
            (3  , "3 : " + account.partition_name3),
            (4  , "4 : " + account.partition_name4),
            (5  , "5 : " + account.partition_name5),
            (6  , "6 : " + account.partition_name6),
            (7  , "7 : " + account.partition_name7),
            (8  , "8 : " + account.partition_name8),
            (9  , "9 : " + account.partition_name9),
            (10 , "10 : " + account.partition_name10),
        )