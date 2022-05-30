import base64
import string

def base64_encode(input: string) -> string:
    """
    Return base64-encoded string for a given input string value
    :param input: input string value
    "return: base64 encoded string value
    """
    encodedBytes = base64.b64encode(input.encode("utf-8"));
    return str(encodedBytes, "utf-8");

def base64_decode(input: string) -> string:
    """
    Return base64-decoded string for a given input string value
    :param input: base64 encoded string value
    "return: resultant string value
    """
    encodedBytes = base64.b64decode(input.encode("utf-8"));
    return str(encodedBytes, "utf-8");

def ascii_encode(input: string,  errorType="strict") -> string:
    """
    Return ascii encoded byte value for a given input string value
    :param input: input string value
    :param errorType: type of error mechanism - strict, ignore, replace, backslashreplace, namereplace, xmlcharrefreplace
    "return: ascii encoded byte value
    """
    return input.encode("ascii", errors=errorType);

def ascii_decode(input: string, errorType="strict") -> string:
    """
    Return decoded string for a given ascii encoded input byte value
    :param input: input ascii encoded string value
    :param errorType: type of error mechanism - strict, ignore, replace, backslashreplace, namereplace, xmlcharrefreplace
    "return: restultant string value
    """
    return input.decode("ascii", errors=errorType);

def base64_urlsafe_encode(input: string) -> string:
    """
    Return base64-encoded value for a given input string value; supports +, / replaced with -,_ 
    :param input: input string value
    "return: base64 encoded string value
    """
    encodedBytes = base64.urlsafe_b64encode(data.encode("utf-8"));
    return str(encodedBytes, "utf-8");

def base64_urlsafe_decode(input: string) -> string:
    """
    Return base64-decoded string for a given input string value; supports +, / replaced with -,_ 
    :param input: base64 encoded string value
    "return: resultant string value
    """
    encodedBytes = base64.urlsafe_b64decode(input.encode("utf-8"));
    return str(encodedBytes, "utf-8");