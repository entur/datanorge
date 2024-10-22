from datacatalogtordf import Catalog
from national_stop_registry.national_stop_registry_dataset import national_stop_registry_dataset
from national_stop_registry.national_stop_registry_api import national_stop_registry_data_service

def main():

    # Create catalog object
    enturCatalog = Catalog()
    enturCatalog.identifier = "https://entur.no/"
    enturCatalog.title = {"en": "Entur Data Catalog"}

    # Add datasets and services to the catalog
    enturCatalog.datasets.append(national_stop_registry_dataset)
    enturCatalog.services.append(national_stop_registry_data_service)

    # Get RDF representation in Turtle format
    rdf = enturCatalog.to_rdf()

    # Print RDF in TTL format
    print(rdf.decode("utf-8"))

if __name__ == "__main__":
    main()