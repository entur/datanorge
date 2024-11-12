from datacatalogtordf import DataService, Contact

from src.constants import Theme, MediaType

BASE_URL = "https://hcreg.atlas.vegvesen.no"

def svv_contact():
    contact = Contact()
    contact.identifier = "brukerstotte@vegvesen.no/sd-test/"
    contact.email = "brukerstotte@vegvesen.no"
    return contact

def create_hc_register_kontroll():
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = f"{BASE_URL}/hc-registeret_gyldigstatus_bedrift/kontroller/"
    data_service.identifier = f"{BASE_URL}/hc-registeret_gyldigstatus_bedrift/kontroller/sd-test/"
    data_service.title = {
        "no": "Register for parkeringstillatelser - endepunkt for kontroll"
    }

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    #data_service.keyword = {"nb": "sanntid,rutetider,reiseplanlegging"}
    data_service.media_types = [MediaType.JSON.value]
    data_service.contactpoint = svv_contact()
    data_service.theme = [Theme.TRANSPORT.value]
    #data_service.servesdatasets = datasets
    data_service.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    # national_stop_registry_dataset.was_generated_by
    # national_stop_registry_dataset.distributions
    # national_stop_registry_dataset.spatial
    # national_stop_registry_dataset.temporal
    # data_service.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    data_service.description = {
        "no": "Et API som brukes for å gjøre oppslag på gyldighet til parkeringstillatelser. Det er kun parkeringstilbydere som kan søke om tilgang."
    }
    data_service.endpointDescription = "https://hcreg.atlas.vegvesen.no/v3/api-docs"
    data_service.landing_page = ["https://www.vegvesen.no/om-oss/om-organisasjonen/apne-data/et-utvalg-apne-data/hc-reg/"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service

def create_hc_register_internbruker():
    data_service = DataService()

    # Obligatory - https://data.norge.no/specification/dcat-ap-no#Datasett-obligatoriske-egenskaper
    data_service.endpointURL = f"{BASE_URL}/hc-registeret_internbruker/"
    data_service.identifier = f"{BASE_URL}/hc-registeret_internbruker/sd-test/"
    data_service.title = {
        "no": "Register for parkeringstillatelser - endepunkt for kommuner"
    }

    # Recomended - https://data.norge.no/specification/dcat-ap-no#Datasett-anbefalte-egenskaper
    #data_service.keyword = {"nb": "sanntid,rutetider,reiseplanlegging"}
    data_service.media_types = [MediaType.JSON.value]
    data_service.contactpoint = svv_contact()
    data_service.theme = [Theme.TRANSPORT.value]
    #data_service.servesdatasets = datasets
    data_service.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    # national_stop_registry_dataset.was_generated_by
    # national_stop_registry_dataset.distributions
    # national_stop_registry_dataset.spatial
    # national_stop_registry_dataset.temporal
    # data_service.access_rights = AccessRight.PUBLIC.value

    # Optional - https://data.norge.no/specification/dcat-ap-no#Datasett-valgfrie-egenskaper
    data_service.description = {
        "no": "Et API som benyttes av leverandører av parkeringssystemer <b>på vegne av en kommunene</b> til å melde inn nye parkeringstillatelser for forflytningshemmede eller endringer i disse."
    }
    data_service.endpointDescription = "https://hcreg.atlas.vegvesen.no/v3/api-docs"
    data_service.landing_page = ["https://www.vegvesen.no/om-oss/om-organisasjonen/apne-data/et-utvalg-apne-data/hc-reg/"]
    # national_stop_registry_dataset.modification_date
    # national_stop_registry_dataset.is_referenced_by

    return data_service