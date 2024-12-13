from distutils.command.register import register

from datacatalogtordf import Catalog

from src.fakedoortestvirksomhet.resources.test import create_test_dataset


def main():
    # Create catalog object
    catalog = Catalog()
    catalog.identifier = "https://www.test-virksomhet.no/"
    catalog.title = {"no": "Testkatalog"}
    catalog.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    catalog.description = {"no": "Testkatalog"}

    # Add datasets and services to the catalog



    catalog.datasets.extend([
        create_test_dataset(),
    ])

    # Get RDF representation in Turtle format
    rdf = catalog._to_graph(
        True,
        True,
    )


    serialized_rdf = rdf.serialize(format="turtle", encoding="utf-8")

    # Print RDF in TTL format
    print(serialized_rdf.decode("utf-8"))
    return serialized_rdf.decode("utf-8")


if __name__ == "__main__":
    main()
