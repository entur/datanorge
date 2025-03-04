from datacatalogtordf import DataService, Dataset

from src.constants import AccessRight, ENTUR_DATANORGE_PAGE, Theme, MediaType
from src.contact import get_contact


def create_station_distances_service(datasets: [Dataset] = []):
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = "https://api.entur.io/distance-ten/"
    data_service.identifier = "https://developer.entur.org/pages-open-distance-ten-api"
    data_service.title = {
        "en": "Station Distances"
    }

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    data_service.keyword = {"nb": "sanntid,rutetider,reiseplanlegging"}
    data_service.media_types = [MediaType.JSON.value]
    data_service.contactpoint = get_contact()
    data_service.theme = [Theme.TRANSPORT.value]
    data_service.servesdatasets = datasets
    data_service.publisher = ENTUR_DATANORGE_PAGE
    # national_stop_registry_dataset.was_generated_by
    # national_stop_registry_dataset.distributions
    # national_stop_registry_dataset.spatial
    # national_stop_registry_dataset.temporal
    data_service.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    data_service.description = {
        "en": "This service handles distances between railway stations, measured along the track. It has an open API for looking up distances, and an internal API for data maintenance."
    }
    data_service.endpointDescription = "https://developer.entur.org/pages-open-distance-ten-api"
    data_service.landing_page = ["https://developer.entur.org/pages-open-distance-ten-api"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service