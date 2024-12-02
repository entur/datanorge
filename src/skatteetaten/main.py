from distutils.command.register import register

from datacatalogtordf import Catalog

from src.SVV.resources.hc_register import create_hc_register_internbruker, create_hc_register_kontroll
from src.skatteetaten.resources.tenor_api import create_tenor_api


def main():
    # Create catalog object
    enturCatalog = Catalog()
    enturCatalog.identifier = "Tenor@skatteetaten.no/catalog/sd-test/"
    enturCatalog.title = {"no": "Testkatalog for Tenor av samferdselsdata"}
    enturCatalog.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    enturCatalog.description = {"no": "Testkatalog for Tenor av samferdselsdata"}

    # Add datasets and services to the catalog



    enturCatalog.services.extend([
        create_tenor_api(),
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
