s1 = '  \n \033[91m'
s2 = '  \033[33m'
s3 = '  \n \033[0m'


def errorHTTP(message, text, route, **kwargs):
    try:
        title = text['id']
    except Exception:
        try:
            title = text['status']
        except Exception:
            title = 'ERROR'
    try:
        t = s1 + title + ': ' + s2 + text['message'] + ' ' + str(text['meta']['errors']) + s3
    except Exception:
        try:
            t = s1 + title + ': ' + s2 + text['message'] + s3
        except Exception:
            t = s1 + title + ': ' + s2 + message + s3
    finally:
        print('\n' + t + '\n')
        print('\n' + route + '\n')
        return ("ERROR: HTTP STATUS CODE " + message)
