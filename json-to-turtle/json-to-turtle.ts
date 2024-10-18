import * as rdflib from 'rdflib';

// Define namespaces
const PRODUCTS = rdflib.Namespace("https://data.entur.no/domain/public-transport-data/product/");
const DEVELOPER = rdflib.Namespace("https://developer.entur.org/");
const DCAT = rdflib.Namespace("http://www.w3.org/ns/dcat#");
const DCTERMS = rdflib.Namespace("http://purl.org/dc/terms/");
const RDF = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#");

// Define interfaces for the JSON structure
interface DataService {
    uri: string;
    title: { [lang: string]: string };
    endpointURL: string;
    description: { [lang: string]: string };
    landingPage: string;
    format: string;
    publisher: string;
    theme: string;
    identifier: string;
}

interface JsonData {
    catalog: { uri: string };
    dataServices: DataService[];
}

// Define the function to convert JSON to DCAT
function jsonToDcat(jsonData: JsonData): string | undefined {
    const g = rdflib.graph();

    // Bind namespaces
    const catalog = rdflib.namedNode(jsonData.catalog.uri);
    g.add(catalog, RDF('type'), DCAT('Catalog'));

    // Loop through data services
    jsonData.dataServices.forEach(service => {
        const serviceUri = rdflib.namedNode(service.uri);
        g.add(catalog, DCAT('service'), serviceUri);
        g.add(serviceUri, RDF('type'), DCAT('DataService'));

        // Support multiple languages for title and description
        if (service.title) {
            for (const lang in service.title) {
                g.add(serviceUri, DCTERMS('title'), rdflib.literal(service.title[lang], lang));
            }
        }

        if (service.description) {
            for (const lang in service.description) {
                g.add(serviceUri, DCTERMS('description'), rdflib.literal(service.description[lang], lang));
            }
        }

        g.add(serviceUri, DCAT('endpointURL'), rdflib.namedNode(service.endpointURL));
        g.add(serviceUri, DCAT('landingPage'), rdflib.namedNode(service.landingPage));
        g.add(serviceUri, DCTERMS('format'), rdflib.namedNode(service.format));
        g.add(serviceUri, DCTERMS('publisher'), rdflib.namedNode(service.publisher));
        g.add(serviceUri, DCAT('theme'), rdflib.namedNode(service.theme));
        g.add(serviceUri, DCTERMS('identifier'), rdflib.literal(service.identifier));
    });

    // Serialize to Turtle format
    return rdflib.serialize(null, g, null, 'text/turtle');
}

// Example JSON data with type
const jsonData: JsonData = {
    catalog: {
        uri: "https://entur.no/"
    },
    dataServices: [
        {
            uri: "https://developer.entur.org/timetable",
            title: {
                en: "Timetable"
            },
            endpointURL: "https://api.entur.io/timetable-public/v1",
            description: {
                en: `API for checking the status of timetable data imports. The endpoint returns the date of the latest successful import of timetable data into Entur's systems for each data provider. Data providers are identified by their codespaces

This import date is also displayed in the list of NeTEx files available on Entur Open Data Portal. Additionally, the import date is stored in each NeTEx archive available on this page, in the "created" timestamp of the CompositeFrame. For example: created="2019-05-29T12:59:32.202"

The date returned by this service is the original import date, i.e. the date Entur received the source dataset from the data provider. It may be different from the creation date of the archives listed on NeTEx files, since these archives are regenerated every day through a filtering process that removes obsolete data.

Base URL: https://api.entur.io/timetable-public/v1
Wildcard definitions necessary to get Jetty to match authorization filters to endpoints with path params`
            },
            landingPage: "https://developer.entur.org/pages-timetable-timetable",
            format: "http://publications.europa.eu/resource/authority/file-type/JSON",
            publisher: "https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/210841962",
            theme: "http://publications.europa.eu/resource/authority/data-theme/GOVE",
            identifier: "https://developer.entur.org/pages-timetable-timetable"
        }
    ]
};

// Convert and print DCAT in Turtle
console.log(jsonToDcat(jsonData));
