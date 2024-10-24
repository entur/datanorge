from datacatalogtordf import DataService, Dataset

from src.constants import AccessRight, ENTUR_DATANORGE_PAGE, Theme, MediaType
from src.contact import get_contact


def create_timetable_data_service(datasets: [Dataset] = []):
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = "https://api.entur.io/timetable-public/v1"
    data_service.identifier = "https://developer.entur.org/timetable"
    data_service.title = {
        "en": "Timetable data"
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
        "en": "Entur operates the national registry for timetable data for all public transport in Norway, collecting data from 60 public transportation operators. This data is open and free of use for app and service developers."
    }
    data_service.endpointDescription = "https://developer.entur.org/timetable-import-info-v1"
    data_service.landing_page = ["https://developer.entur.org/pages-timetable-timetable"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service

def create_timetable_dataset():
    dataset = Dataset()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    dataset.description = {
        "en": "Part of our mission statement is to share our data with anyone who wants it, for free. This page lists all our timetables, and stop place data dumps which are updated daily. All data dumps have permanent URL's and come as NeTEx or GTFS datasets. NeTEx is the official format for public transport data in Norway and is the most complete in terms of available data. GTFS is a downstream format with only a limited subset of the total data, but we generate datasets for it anyway since GTFS can be easier to use and has a wider distribution among international public transport solutions. GTFS sets come in extended and basic versions."
    }
    dataset.identifier = "https://developer.entur.org/stops-and-timetable-data" 
    dataset.theme = [Theme.TRANSPORT.value]
    dataset.title = {
        "en": "Timetable data"
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

def create_time_table_resources():
    dataset = create_timetable_dataset()
    data_service = create_timetable_data_service([dataset])
    return dataset, data_service