"""developer:national_stop_registry_api
    dcat:landingPage <https://developer.entur.org/pages-nsr-nsr>;
    dcat:servesDataset products:national_stop_registry;
    dct:format      <http://publications.europa.eu/resource/authority/file-type/JSON>;
    dct:publisher   <https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/210841962> ;
    dcat:theme      <http://publications.europa.eu/resource/authority/data-theme/GOVE>;
    dct:identifier  "https://developer.entur.org/stop-places"."""
from rdflib import URIRef

from src.constants import ENTUR_DATANORGE_PAGE, AccessRight, Format, Theme
from src.contact import contact
from datacatalogtordf import DataService
from src.national_stop_registry import national_stop_registry_dataset


national_stop_registry_data_service = DataService()

# Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
national_stop_registry_data_service.endpointURL = "https://api.entur.io/stop-places/v1/read"
national_stop_registry_data_service.identifier = "https://developer.entur.org/stop-place"
national_stop_registry_data_service.title = {
    "nb": "Norsk stoppestedregister",
    "en": "National Stop Registry"
}

# Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
national_stop_registry_data_service.keyword = {"en" : "National Stop Registry"}
national_stop_registry_data_service.media_types = [Format.JSON.value]
national_stop_registry_data_service.contactpoint = contact
national_stop_registry_data_service.theme = [Theme.GOVE.value]
national_stop_registry_data_service.servesdatasets = [national_stop_registry_dataset]
national_stop_registry_data_service.publisher = ENTUR_DATANORGE_PAGE

# dataset.concept - Hvor er denne blitt av??
# national_stop_registry_dataset.was_generated_by = None
# national_stop_registry_dataset.distributions = None # TODO
# national_stop_registry_dataset.spatial = None
# dataset.follows - Hvor er denne? - Datasett: følger (cpsv:follows)
# national_stop_registry_dataset.temporal = None

national_stop_registry_data_service.access_rights = AccessRight.PUBLIC.value

# Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
national_stop_registry_data_service.deescription = {
    "en": "This API is the core service for journey planning and uses OpenTripPlanner software to provide departure boards for individual stops, and point-to-point journey planning for all public transport in Norway, including real-time information, regardless of transport mode, or operator. All data is presented as a Transmodel-based GraphQL-API."
}
national_stop_registry_data_service.endpointDescription = "https://developer.entur.org/stop-places-v1-read"
# other identifier? https://data.norge.no/specification/dcat-ap-no#Datasett-annenIdentifikator
# national_stop_registry_dataset.modification_date = None
# national_stop_registry_dataset.is_referenced_by = None # TODO
