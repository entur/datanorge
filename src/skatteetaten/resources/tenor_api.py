from datacatalogtordf import DataService, Contact

from src.constants import Theme, MediaType, AccessRight


def tenor_contact():
    contact = Contact()
    contact.identifier = "Tenor@skatteetaten.no/sd-test/"
    contact.email = "Tenor@skatteetaten.no"
    return contact

def create_tenor_api():
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = f"https://testdata.api.skatteetaten.no/api/testnorge/v2/soek/"
    data_service.identifier = f"https://testdata.api.skatteetaten.no/api/testnorge/v2/soek/sd-test/"
    data_service.title = {
        "no": "Testdata søk API"
    }

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    data_service.keyword = {"nb": "tenor, testdatasøk"}
    data_service.media_types = [MediaType.JSON.value, MediaType.PLAIN_TEXT.value]
    data_service.contactpoint = tenor_contact()
    #data_service.servesdatasets = datasets
    data_service.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    # national_stop_registry_dataset.was_generated_by
    # national_stop_registry_dataset.distributions
    # national_stop_registry_dataset.spatial
    # national_stop_registry_dataset.temporal
    # data_service.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    data_service.description = {
        "no": "Tenor testdatasøk gir deg muligheten til å søke i syntetiske testdata fra Test-Norge, og via API-et kan virksomheter integrere mot fra sine automatiske verdikjedetester for søk i testdataene."
    }
    data_service.endpointDescription = "https://skatteetaten.github.io/testnorge-tenor-dokumentasjon/api/openapi-soek-api/"
    data_service.landing_page = ["https://skatteetaten.github.io/testnorge-tenor-dokumentasjon"]
    # national_stop_registry_dataset.modification_date
    #data_service.is_referenced_by = ["https://skatteetaten.github.io/testnorge-tenor-dokumentasjon/#hvordan-s%C3%B8ke-via-api-et"]

    return data_service