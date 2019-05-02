import config


def log(message: str, write_to_file: bool = False):
    if config.log_to_console:
        # TODO Implement file write log or something
        print('[DAL] %s' % message)
