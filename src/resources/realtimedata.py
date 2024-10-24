from datacatalogtordf import DataService, Dataset

from src.constants import AccessRight, ENTUR_DATANORGE_PAGE, Theme, MediaType
from src.contact import get_contact


def create_realtime_data_service(datasets: [Dataset] = []):
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = "https://api.entur.io/realtime/v1"
    data_service.identifier = "https://developer.entur.org/pages-real-time-intro"
    data_service.title = {
        "en": "Real-Time Data"
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
        "en": "These APIs allow your server to subscribe to real-time data from all included real-time feeds in Norway on SIRI 2.0. It is available as SIRI XML, SIRI Lite (REST) and GTFS-RT. These services include only real-time data and not any basic journey planner information. If you are creating an end-user service such as a journey planner, the JourneyPlanner API is a better choice."
    }
    data_service.endpointDescription = "https://developer.entur.org/pages-real-time-api"
    data_service.landing_page = ["https://developer.entur.org/pages-real-time-intro"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service