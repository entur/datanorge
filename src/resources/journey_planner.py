from datacatalogtordf import Dataset, DataService

from src.constants import Format, Theme, ENTUR_DATANORGE_PAGE, AccessRight
from src.contact import get_contact


def create_journey_planner_service(datasets: [Dataset] = []):
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = "https://api.entur.io/journey-planner/v3/graphql"
    data_service.identifier = "https://developer.entur.org/pages-journeyplanner-journeyplanner"
    data_service.title = {
        "en": "Journey Planner"
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
        "en": "This API is the core service for journey planning and uses OpenTripPlanner software to provide departure boards for individual stops, and point-to-point journey planning for all public transport in Norway, including real-time information, regardless of transport mode, or operator. All data is presented as a Transmodel-based GraphQL-API. Base URL: https://api.entur.io/journey-planner/v3/graphql . To make it easier for our users to construct valid API-queries, we have an IDE for the API where you also find the documentation. GraphQL IDE: https://api.entur.io/graphql-explorer/journey-planner-v3 . Are you new to GraphQL? You can read more about it here: https://graphql.org/"
    }
    data_service.endpointDescription = "https://developer.entur.org/pages-journeyplanner-journeyplanner"
    data_service.landing_page = ["https://developer.entur.org/pages-journeyplanner-journeyplanner"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service