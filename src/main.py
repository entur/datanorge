from datacatalogtordf import Catalog

from src.constants import ENTUR_DATANORGE_PAGE
from src.resources.geocoder import create_geocoder_data_service
from src.resources.journey_planner import create_journey_planner_service
from src.resources.mobility import create_mobility_service
from src.resources.national_stop_registry import get_national_stop_registry_resourses
from src.resources.realtimedata import create_realtime_data_service
from src.resources.station_distances import create_station_distances_service
from src.resources.timetable import create_time_table_resources


def main():
    # Create catalog object
    enturCatalog = Catalog()
    enturCatalog.identifier = "https://entur.org/"
    enturCatalog.title = {"en": "Entur Data Catalog"}
    enturCatalog.publisher = ENTUR_DATANORGE_PAGE
    enturCatalog.description = {"en": "Entur data catalogue"}

    # Add datasets and services to the catalog
    national_stop_registry_dataset, national_stop_registry_data_service = get_national_stop_registry_resourses()
    geocoder_data_service = create_geocoder_data_service()
    journey_planner_service = create_journey_planner_service()
    timetable_dataset, timetable_data_service = create_time_table_resources()
    realtime_data_service = create_realtime_data_service()
    station_distances_data_service = create_station_distances_service()
    mobility_data_service = create_mobility_service()

    enturCatalog.datasets.extend([
        national_stop_registry_dataset,
        timetable_dataset,
    ])
    enturCatalog.services.extend([
        national_stop_registry_data_service,
        geocoder_data_service,
        journey_planner_service,
        timetable_data_service,
        realtime_data_service,
        station_distances_data_service,
        mobility_data_service
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
