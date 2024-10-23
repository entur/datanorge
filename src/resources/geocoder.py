from datacatalogtordf import Dataset, DataService

from src.constants import Format, Theme, ENTUR_DATANORGE_PAGE, AccessRight
from src.contact import get_contact


def create_geocoder_data_service(datasets: [Dataset] = []):
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = "https://api.entur.io/geocoder/v1/"
    data_service.identifier = "https://developer.entur.org/pages-geocoder-intro"
    data_service.title = {
        "en": "Geocoder"
    }

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    data_service.keyword = {"nb": "sanntid,rutetider,reiseplanlegging"}
    #data_service.media_types = [Format.JSON.value]
    data_service.contactpoint = get_contact()
    data_service.theme = [Theme.TRANSPORT.value]
    data_service.servesdatasets = datasets
    data_service.publisher = ENTUR_DATANORGE_PAGE
    # dataset.concept
    # national_stop_registry_dataset.was_generated_by
    # national_stop_registry_dataset.distributions
    # national_stop_registry_dataset.spatial
    # national_stop_registry_dataset.temporal
    data_service.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    data_service.description = {
        "en": """The Geocoder API can be used to query addresses, Points Of Interest (POI) and public transport stops. The primary purpose of the geocoder is to find the start- and end points for queries to the journey planner API through an autosuggest interface.

        The following query will return a list of destination- or arrival points containing POI's, addresses and stops that match the string "sons":
        
        https://api.entur.io/geocoder/v1/autocomplete?text=sons&lang=en"""
    }
    data_service.endpointDescription = "https://developer.entur.org/pages-geocoder-api"
    data_service.landing_page = ["https://developer.entur.org/pages-geocoder-intro"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service