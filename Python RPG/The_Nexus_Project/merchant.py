### Merchant Creation###
def describe_merchant(**kwargs):
    kwargs.get("discount", 0)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return "Profile Complete"
###Gold Calculator###
def sum_gold(*args):
    return sum(args)
