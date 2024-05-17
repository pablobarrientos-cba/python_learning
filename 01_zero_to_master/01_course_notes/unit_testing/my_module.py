def do_stuff(num):
    try:
        return int(num) ** 2
    except ValueError as err:
        return err
