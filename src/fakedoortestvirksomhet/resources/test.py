from datacatalogtordf import DataService, Contact, Dataset

from src.constants import Theme, MediaType

BASE_URL = "https://endepunkt.no"

def create_test_dataset():
    dataset = Dataset()
    dataset.identifier = "https://test-data/identifikator-for-datasettet"
    dataset.title = {
        "no": "Statistikk over Interessemeldinger for tilgang til dataressurser"
    }
    dataset.publisher = "https://staging.fellesdatakatalog.digdir.no/organizations/210841962"
    dataset.description = {
        "no": """
Sikt sin løsning for søknad og interesse for data får inn interessemeldinger for dataressurser som ennå ikke er klare for deling. Interessemeldingene inkluderer informasjon om hvem som ønsker tilgang (privatperson eller virksomhet), formålet med forespørselen, og hvilke dataressurser som etterspørres. Trykk på meld interesse, dersom en aggregert versjon at disse dataene er interessante for deg!

Bakgrunn:

Før man kan dele data, må man gjennom juridiske vurderinger for å avklare hvem data kan deles med, og hvilke personvernshensyn som må ivaretas. I tillegg kreves det tekniske prosesser som å hente ut, klargjøre og distribuere dataene. Dette er ressurskrevende, og derfor er det viktig å først finne ut om det faktisk finnes et behov for dataene. Eksisterer ikke behovet, bør man heller ikke bruke tid og ressurser på disse prosessene.

For å løse dette kan Sikt sin søknadsløsning brukes som en enkel måte å samle inn interessemeldinger for dataressurser som ikke er klare for deling. Brukere kan registrere sitt behov ved å klikke på "Gi meg tilgang" og skrive inn formålet med forespørselen.

Dersom det er mange nok som ønsker tilgang til en dataressurs, kan dette brukes som grunnlag for å prioritere de juridiske og tekniske prosessene som trengs for å gjøre dataene tilgjengelige. Samtidig gir dette en måte å samle innsikt i hvilke data som faktisk er etterspurt, uten at de trenger å være klare for deling på forhånd. Det er altså en datadreven tilnærming til datadeling 🤓

Trykk på "Meld interesse" for å vise at du ønsker tilgang til en aggregert statistikk over interessemeldinger. Din interesse kan bidra til å prioritere utarbeidelsen av denne statistikken og gi innsikt i hvilke dataressurser som er mest etterspurt. Sammen kan vi skape en mer behovsdrevet og effektiv tilnærming til datadeling!
"""
    }
    dataset.theme = [Theme.TRANSPORT.value, Theme.TRANSPORT_MOBILITETSTILBUD.value]

    return dataset