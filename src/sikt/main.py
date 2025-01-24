from distutils.command.register import register

from datacatalogtordf import Catalog

from resources.interessemelding_fakedoor import create_test_dataset


def main():
    # Create catalog object
    catalog = Catalog()
    catalog.identifier = "https://sikt.no/test-datasamarbeidet"
    catalog.title = {"no": "Sikt – testkatalog for interessemeldinger"}
    catalog.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    catalog.description = {"no": "Testkatalog for interessemeldinger"}

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
