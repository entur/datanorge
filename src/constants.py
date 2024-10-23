from enum import Enum

from rdflib import URIRef

ENTUR_DATANORGE_PAGE = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"


class AccessRight(Enum):
    PUBLIC = URIRef("http://publications.europa.eu/resource/authority/access-right/PUBLIC")
    RESTRICTED = URIRef("http://publications.europa.eu/resource/authority/access-right/RESTRICTED")
    NON_PUBLIC = URIRef("http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC")

class Format(Enum):
    JSON = URIRef("http://publications.europa.eu/resource/authority/file-type/JSON")

class Theme(Enum):
    GOVE = URIRef("http://publications.europa.eu/resource/authority/data-theme/GOVE")
    TRANSPORT = URIRef("http://publications.europa.eu/resource/authority/data-theme/TRAN")