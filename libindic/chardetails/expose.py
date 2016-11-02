from chardetails.core import CharDetails


def chardetails_getdetails(text):
    C = CharDetails()
    result = C.getdetails(text)
    # Conflict with the signature.
    del result['Characters']
    return result


def get_details():
    return [chardetails_getdetails, str, {str: {str: str}}]
