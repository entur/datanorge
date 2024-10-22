from datacatalogtordf import Catalog

from national_stop_registry.national_stop_registry import get_national_stop_registry_resourses


def main():

    # Create catalog object
    enturCatalog = Catalog()
    enturCatalog.identifier = "https://entur.no/"
    enturCatalog.title = {"en": "Entur Data Catalog"}

    # Add datasets and services to the catalog
    (national_stop_registry_dataset, national_stop_registry_data_service) = get_national_stop_registry_resourses()

    enturCatalog.datasets.append(national_stop_registry_dataset)
    enturCatalog.services.append(national_stop_registry_data_service)

    # Get RDF representation in Turtle format
    rdf = enturCatalog.to_rdf()

    # Print RDF in TTL format
    print(rdf.decode("utf-8"))

if __name__ == "__main__":
    main()