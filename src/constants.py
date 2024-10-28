from enum import Enum

from rdflib import URIRef

ENTUR_DATANORGE_PAGE = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"


class AccessRight(Enum):
    PUBLIC = URIRef("http://publications.europa.eu/resource/authority/access-right/PUBLIC")
    RESTRICTED = URIRef("http://publications.europa.eu/resource/authority/access-right/RESTRICTED")
    NON_PUBLIC = URIRef("http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC")

class Format(Enum):
    JSON = URIRef("http://publications.europa.eu/resource/authority/file-type/JSON")

class MediaType(Enum):
    JSON = URIRef("https://www.iana.org/assignments/media-types/application/json")

class Theme(Enum):
    GOVE = URIRef("http://publications.europa.eu/resource/authority/data-theme/GOVE")
    TRANSPORT = URIRef("http://publications.europa.eu/resource/authority/data-theme/TRAN")
    TRANSPORT_RUTEINFORMASJON = URIRef("https://psi.norge.no/los/ord/ruteinformasjon")
    TRANSPORT_MOBILITETSTILBUD = URIRef("https://psi.norge.no/los/tema/mobilitetstilbud")
    TRANSPORT_TRAFIKKINFORMASJON = URIRef("https://psi.norge.no/los/tema/trafikkinformasjon")

class Location(Enum):
    NORWAY = URIRef("https://data.geonorge.no/administrativeEnheter/nasjon/id/173163")