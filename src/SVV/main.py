from distutils.command.register import register

from datacatalogtordf import Catalog

from src.SVV.resources.hc_register import create_hc_register_internbruker, create_hc_register_kontroll


def main():
    # Create catalog object
    enturCatalog = Catalog()
    enturCatalog.identifier = "https://www.vegvesen.no/sd-test/"
    enturCatalog.title = {"no": "Testkatalog for Statens vegvesen av samferdselsdata"}
    enturCatalog.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    enturCatalog.description = {"en": "Testkatalog for Statens vegvesen av samferdselsdata"}

    # Add datasets and services to the catalog



    enturCatalog.services.extend([
        create_hc_register_internbruker(),
        create_hc_register_kontroll(),
    ])

    # Get RDF representation in Turtle format
    rdf = enturCatalog._to_graph(
        True,
        True,
    )


    serialized_rdf = rdf.serialize(format="turtle", encoding="utf-8")

    # Print RDF in TTL format
    print(serialized_rdf.decode("utf-8"))
    return serialized_rdf.decode("utf-8")


if __name__ == "__main__":
    main()
