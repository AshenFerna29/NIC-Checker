def nic(nic_num):
    if len(nic_num)== 10:
        return'old'
    elif len(nic_num)== 12:
        return'new'
    else:
        return'invalid id'
