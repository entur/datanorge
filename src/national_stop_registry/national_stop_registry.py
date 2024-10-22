from datacatalogtordf import DataService, Dataset
from rdflib import  URIRef

from src.constants import AccessRight, ENTUR_DATANORGE_PAGE, Format, Theme
from src.contact import contact


def create_api(datasets: [Dataset]):
    national_stop_registry_data_service = DataService()
    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    national_stop_registry_data_service.endpointURL = "https://api.entur.io/stop-places/v1/read"
    national_stop_registry_data_service.identifier = "https://developer.entur.org/stop-place"
    national_stop_registry_data_service.title = {
        "nb": "Norsk stoppestedregister",
        "en": "National Stop Registry"
    }
    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    national_stop_registry_data_service.keyword = {"nb": "sanntid,rutetider,reiseplanlegging"}
    national_stop_registry_data_service.media_types = [Format.JSON.value]
    national_stop_registry_data_service.contactpoint = contact
    national_stop_registry_data_service.theme = [Theme.GOVE.value]
    national_stop_registry_data_service.servesdatasets = datasets
    national_stop_registry_data_service.publisher = ENTUR_DATANORGE_PAGE
    # dataset.concept - Hvor er denne blitt av??
    # national_stop_registry_dataset.was_generated_by = None
    # national_stop_registry_dataset.distributions = None # TODO
    # national_stop_registry_dataset.spatial = None
    # dataset.follows - Hvor er denne? - Datasett: følger (cpsv:follows)
    # national_stop_registry_dataset.temporal = None
    national_stop_registry_data_service.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    national_stop_registry_data_service.description = {
        "en": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place."
    }
    national_stop_registry_data_service.endpointDescription = "https://developer.entur.org/stop-places-v1-read"
    national_stop_registry_data_service.landing_page = ["https://developer.entur.org/pages-nsr-nsr"]
    # other identifier? https://data.norge.no/specification/dcat-ap-no#Datasett-annenIdentifikator
    # national_stop_registry_dataset.modification_date = None
    # national_stop_registry_dataset.is_referenced_by = None # TODO

    return national_stop_registry_data_service

def get_dataset():
    dataset = Dataset()
    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    dataset.description = {
        "nb": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place.",
        "en": "National Stop Register (NSR) is the master database for public transport stops in Norway and is primarily used to store and redistribute detailed information regarding the infrastructure of a stop place."
    }
    dataset.identifier = "https://stoppested.entur.org/"
    dataset.theme = [URIRef("http://publications.europa.eu/resource/authority/data-theme/GOVE")]
    dataset.title = {
        "nb": "Norsk stoppestedregister",
        "en": "National Stop Registry"
    }
    dataset.publisher = ENTUR_DATANORGE_PAGE
    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    # dataset.concept - Hvor er denne blitt av??
    # dataset.was_generated_by = None
    # dataset.distributions = None # TODO
    # dataset.spatial = None
    # dataset.keyword = None # Keyword? I entall?
    # dataset.follows - Hvor er denne? - Datasett: følger (cpsv:follows)
    dataset.contactpoint = contact
    # dataset.temporal = None
    dataset.access_rights = AccessRight.PUBLIC.value
    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    # other identifier? https://data.norge.no/specification/dcat-ap-no#Datasett-annenIdentifikator
    # dataset.modification_date = None
    # dataset.is_referenced_by = None # TODO
    return dataset

def get_national_stop_registry_resourses():
    national_stop_registry_dataset = get_dataset()
    return (national_stop_registry_dataset, create_api([national_stop_registry_dataset]))
