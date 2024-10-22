from src.constants import ENTUR_DATANORGE_PAGE, AccessRight
from src.contact import contact
from datacatalogtordf import Dataset
from rdflib import URIRef

national_stop_registry_dataset = Dataset()

# Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
national_stop_registry_dataset.description = {
    "nb": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place.",
    "en": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place."
}
national_stop_registry_dataset.identifier = "https://data.entur.no/domain/public-transport-data/product/national_stop_registry/"
national_stop_registry_dataset.theme = [URIRef("http://publications.europa.eu/resource/authority/data-theme/GOVE")]
national_stop_registry_dataset.title = {
    "nb": "Norsk stoppestedregister",
    "en": "National Stop Registry"
}
national_stop_registry_dataset.publisher = ENTUR_DATANORGE_PAGE

# Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
# dataset.concept - Hvor er denne blitt av??
# national_stop_registry_dataset.was_generated_by = None
# national_stop_registry_dataset.distributions = None # TODO
# national_stop_registry_dataset.spatial = None
# national_stop_registry_dataset.keyword = None # Keyword? I entall?
# dataset.follows - Hvor er denne? - Datasett: følger (cpsv:follows)
national_stop_registry_dataset.contactpoint = contact
# national_stop_registry_dataset.temporal = None

national_stop_registry_dataset.access_rights =  AccessRight.PUBLIC.value

# Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
# other identifier? https://data.norge.no/specification/dcat-ap-no#Datasett-annenIdentifikator
# national_stop_registry_dataset.modification_date = None
# national_stop_registry_dataset.is_referenced_by = None # TODO


