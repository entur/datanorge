from datacatalogtordf import DataService, Contact, Dataset

from src.constants import Theme, MediaType

BASE_URL = "https://endepunkt.no"

def create_test_dataset():
    dataset = Dataset()
    dataset.identifier = "https://test-data/identifikator-for-datasettet"
    dataset.title = {
        "no": "Test av fakedoor"
    }
    dataset.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    dataset.description = {
        "no": "Beskrivelse av data."
    }
    dataset.theme = [Theme.TRANSPORT.value, Theme.TRANSPORT_MOBILITETSTILBUD.value]

    return dataset