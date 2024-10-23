from datacatalogtordf import DataService, Dataset

from src.constants import AccessRight, ENTUR_DATANORGE_PAGE, Format, Theme
from src.contact import get_contact


def create_mobility_service(datasets: [Dataset] = []):
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = "https://api.entur.io/mobility/v2/gbfs/v3/"
    data_service.identifier = "https://developer.entur.org/pages-mobility-docs-mobility-v2"
    data_service.title = {
        "en": "Mobility"
    }

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    data_service.keyword = {"nb": "sanntid,rutetider,reiseplanlegging"}
#    data_service.media_types = [Format.JSON.value]
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
        "en": """Aggregation API for shared mobility services."""
    }
    data_service.endpointDescription = "https://developer.entur.org/pages-mobility-docs-mobility-v2"
    data_service.landing_page = ["https://developer.entur.org/pages-mobility-docs-mobility-v2"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service