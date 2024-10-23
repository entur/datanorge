from uuid import uuid4

from datacatalogtordf import DataService, Dataset
from rdflib import  URIRef

from src.constants import AccessRight, ENTUR_DATANORGE_PAGE, Format, Theme
from src.contact import get_contact


def create_data_service(datasets: [Dataset] = []):
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = "https://api.entur.io/stop-places/v1/read"
    data_service.identifier = "https://developer.entur.org/stop-place" + str(uuid4())
    data_service.title = {
        "nb": "Norsk stoppestedregister",
        "en": "National Stop Registry"
    }

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    data_service.keyword = {"nb": "sanntid,rutetider,reiseplanlegging"}
    data_service.media_types = [Format.JSON.value]
    data_service.contactpoint = get_contact()
    data_service.theme = [Theme.GOVE.value]
    data_service.servesdatasets = datasets
    data_service.publisher = ENTUR_DATANORGE_PAGE
    # national_stop_registry_dataset.was_generated_by
    # national_stop_registry_dataset.distributions
    # national_stop_registry_dataset.spatial
    # national_stop_registry_dataset.temporal
    data_service.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    data_service.description = {
        "en": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place."
    }
    data_service.endpointDescription = "https://developer.entur.org/stop-places-v1-read"
    data_service.landing_page = ["https://developer.entur.org/pages-nsr-nsr"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service

def create_dataset():
    dataset = Dataset()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    dataset.description = {
        "nb": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place.",
        "en": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place."
    }
    dataset.identifier = "https://stoppested.entur.org/" + str(uuid4())
    dataset.theme = [URIRef("http://publications.europa.eu/resource/authority/data-theme/GOVE")]
    dataset.title = {
        "nb": "Norsk stoppestedregister",
        "en": "National Stop Registry"
    }
    dataset.publisher = ENTUR_DATANORGE_PAGE

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    # dataset.concept
    # dataset.was_generated_by
    # dataset.distributions
    # dataset.spatial
    # dataset.keyword
    dataset.contactpoint = get_contact()
    # dataset.temporal
    dataset.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    # dataset.modification_date
    # dataset.is_referenced_by
    return dataset

def get_national_stop_registry_resourses():
    national_stop_registry_dataset = create_dataset()
    return national_stop_registry_dataset, create_data_service([national_stop_registry_dataset])
