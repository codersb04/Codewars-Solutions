"""
DESCRIPTION:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
def domain_name(url):
    import re
    pattern=re.compile(r'(https?://|www\.)?(www\.)?([a-zA-Z0-9]+)(\..+)?')
    domain=pattern.sub(r'\3',url)
    return domain