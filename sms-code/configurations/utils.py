import serial.tools.list_ports
from django.utils.translation import gettext as _

from accounts.models import Account, AccountUser

def get_ports():
    ports = serial.tools.list_ports.comports(include_links=False)
    result = {}
    for port in ports:
        result[port.device] = port.name

    return result


def get_action_choices(account_id = -1):

    if account_id == -1:
        return ()
    else:
        account = Account.objects.get(pk=account_id)
        account_users = AccountUser.objects.filter(account=account)

        results = (
            (-1, _("None")),
            (-10, _("Police Number 1") + ": " + str(account.police_number1)),
            (-11, _("Police Number 2") + ": " + str(account.police_number2)),
            (-12, _("Police Number 3") + ": " + str(account.police_number3)),
          
            (-20, _("Fire Dept Number 1")+ ": " + str(account.fire_dept_number1)),
            (-21, _("Fire Dept Number 2")+ ": " + str(account.fire_dept_number2)),
            (-22, _("Fire Dept Number 3")+ ": " + str(account.fire_dept_number3)),
            
            (-30, _("Emergency Number 1")+ ": " + str(account.emergency_number1)),
            (-31, _("Emergency Number 2")+ ": " + str(account.emergency_number2)),
            (-32, _("Emergency Number 3")+ ": " + str(account.emergency_number3)),            
        )
        
        for account_user in account_users:
            results += (
                        (account_user.id + 1000000, account_user.name + " - " + account_user.title1 + ": " + str(account_user.phone_number1)),
                        (account_user.id + 2000000, account_user.name + " - " + account_user.title2 + ": " + str(account_user.phone_number2)),
                        (account_user.id + 3000000, account_user.name + " - " + account_user.title3 + ": " + str(account_user.phone_number3)),
                    )
        
        return results